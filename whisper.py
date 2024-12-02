import argparse
from openai import OpenAI
from pydub import AudioSegment
import tempfile

# Initialize the OpenAI client
client = OpenAI(api_key='xxxxx')

# Argument parsing
parser = argparse.ArgumentParser(description='Process audio file for transcription.')
parser.add_argument('audio_file', help='Path to the audio file')
parser.add_argument('--gpt_post_process', action='store_true', help='Enable GPT-4 post-processing')
parser.add_argument('--output_file', default='transcript.txt', help='Output file path')
args = parser.parse_args()

## Function to split the audio file
def split_audio(file_path, chunk_length_ms):
    # Use from_file to handle different formats, including mp4
    audio = AudioSegment.from_file(file_path)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunks.append(audio[i:i+chunk_length_ms])
    return chunks

def transcribe(audio_chunk):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
        audio_chunk.export(temp_file.name, format='mp3')
        with open(temp_file.name, 'rb') as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file, 
                response_format="text"
            )
        # Check the format of the response and extract text accordingly
        if isinstance(response, str):
            print("Transcription result (string):", response)  # Print the response if it's a string
            return response
        else:
            print("Transcription result (choice):", response.choices[0].text)  # Print the response text from the choice
            return response.choices[0].text

# Function to post-process with GPT-4
def post_process_transcript(transcript, system_prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content

# Main function adjusted to use arguments
def process_audio(file_path, chunk_length_ms, system_prompt, use_gpt_post_process):
    chunks = split_audio(file_path, chunk_length_ms)
    full_transcript = ""
    for chunk in chunks:
        transcript = transcribe(chunk)
        if use_gpt_post_process:
            transcript = post_process_transcript(transcript, system_prompt)
        full_transcript += transcript + "\n"
    return full_transcript

# Updated example usage with arguments
file_path = args.audio_file
chunk_length_ms = 10 * 60 * 1000  # 10 minutes in milliseconds
system_prompt = """
Here is the transcript of a meeting. Please create a concise summary of the topics discussed, decisions made and open points. The summary should include the following:

Topics: A brief overview of the key discussion points.
Decisions: All specific decisions made in the meeting.
Open points: Points that still need to be clarified or dealt with, with corresponding responsibilities and deadlines.
Action items: A list of tasks, who is responsible for them and by when they should be completed.
Answer in the language of the transcript.
Here is the transcript:
"""

full_transcript = process_audio(file_path, chunk_length_ms, system_prompt, args.gpt_post_process)

# Save the transcript to the specified file
with open(args.output_file, "w") as file:
    file.write(full_transcript)
