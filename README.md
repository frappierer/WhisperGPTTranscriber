# WhisperGPTTranscriber
WhisperGPTTranscriber is a Python-based tool that efficiently converts audio files to text using OpenAI's Whisper model and enhances the transcription accuracy with GPT-4 post-processing. It supports large audio files, offers conditional GPT-4 enhancement, and allows customizable output locations.

## Features
- **Audio Transcription**: Utilizes the Whisper model for efficient audio-to-text conversion.
- **GPT-4 Post-Processing**: Offers optional post-processing with GPT-4 for enhanced transcription accuracy or a direct summary of key facts.
- **Large File Support**: Capable of processing audio files larger than the standard size limits of 25 MBs.
- **Customizable Output**: Allows users to specify output file locations.

## Installation
- Install openai and pydub (mp3 handling): ```pip install openai pydub```
- Add the openai key to the .py file
- Change the GPT Model if you want. I am using "gpt-4-1106-preview"

## Usage
_The script takes a while (minutes). Especially when the mp3 is long. As a progress Statement, it will print the transcripts of the "chopped" mp3 into the terminal._

Example: Download any Youtube Video as .mp3. There are a billion converters out there. Like https://notube.cc/de/youtube-app-v103
Then...

This will run the script and save the transcript in the same folder as the .py file:

```python3 whisper.py path/to/audio.mp3```

This will run the script, post-process it and then save the transcript in a designated folder:

```python3 whisper.py path/to/audio.mp3 --gpt_post_process --output_file path/to/output.txt```

## GPT Post-Processing
The GPT post-processing feature in WhisperGPTTranscriber uses OpenAI's GPT-4 model to refine and enhance the transcriptions. After the initial transcription with Whisper, the text is passed through GPT-4, which corrects grammatical errors, clarifies ambiguous language, and ensures proper spelling, especially of specific terms or names.

### Examples of GPT Post-Processing Usage
1. **Technical Meetings**: Improves the accuracy of technical jargon in transcriptions from IT or scientific discussions.
2. **Educational Lectures**: Enhances clarity in transcribed lectures, ensuring correct terminology and coherence.
3. **Business Conferences**: Polishes transcripts of business conferences, focusing on correct names of companies, products, and industry-specific terms.
4. **Medical Dictations**: Ensures medical terms and drug names are accurately transcribed from doctors’ audio notes.
5. **Legal Proceedings**: Refines transcriptions of legal proceedings, where accuracy of names, laws, and legal terminology is crucial.


