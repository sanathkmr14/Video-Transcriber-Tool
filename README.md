# Video Transcriber

A Python-based video and audio transcription tool using OpenAI's Whisper model.

## Features

- 📹 Transcribes video files (mp4, avi, mkv, mov, webm)
- 🎵 Transcribes audio files (mp3, wav, m4a, flac)
- 📝 Outputs transcriptions in both text and JSON formats
- 🎥 Automatically extracts audio from video files before transcription

## Requirements

- Python 3.8+
- OpenAI Whisper
- MoviePy

## Installation

```bash
pip install openai-whisper moviepy
```

## Usage

1. Place your media files in the `Media_Folder/` directory
2. Run the transcription script:

```bash
python Transcription_folder/transcriber.py
```

3. Transcriptions will be saved in the `Transcription_folder/` directory as both `.txt` and `.json` files

## Configuration

Edit the paths in `transcriber.py` to customize input and output directories:

```python
INPUT_FOLDER = "path/to/your/media/files"
OUTPUT_FOLDER = "path/to/output/folder"
```

## Model Selection

By default, the script uses the "tiny" Whisper model for fast processing. You can change this to:
- `tiny` - Fastest, least accurate
- `base` - Balanced speed and accuracy
- `small` - Better accuracy
- `medium` - High accuracy
- `large` - Best accuracy, slowest

Change the model in the script:
```python
model = whisper.load_model("medium")  # or any other model
```
