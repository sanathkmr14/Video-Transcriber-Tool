import os
import whisper
import moviepy.editor as mp
import json

# ✅ Set input and output directories correctly
INPUT_FOLDER = "/Users/harish/Developer/Sanath Kumar/Backups/Code/Video Transcriber/Media_Folder"  # Folder containing media files
OUTPUT_FOLDER = "/Users/harish/Developer/Sanath Kumar/Backups/Code/Video Transcriber/Transcription_folder"  # Folder to save transcriptions

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("🔍 Scanning folder:", INPUT_FOLDER)
print("📂 Files found:", os.listdir(INPUT_FOLDER))

# Supported media file types
AUDIO_EXTENSIONS = (".mp3", ".wav", ".m4a", ".flac")
VIDEO_EXTENSIONS = (".mp4", ".avi", ".mkv", ".mov", ".webm")

# Load Whisper model (smallest model for fast processing)
model = whisper.load_model("tiny")

def transcribe_audio(file_path, output_text_path, output_json_path):
    """Transcribes audio and saves the text and JSON."""
    print(f"🔹 Transcribing: {file_path}")

    # Transcribe the file
    result = model.transcribe(file_path)

    # Save transcription as text
    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    # Save transcription as JSON
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print(f"✅ Saved transcription: {output_text_path}")

def extract_audio(video_path, audio_path):
    """Extracts audio from a video file."""
    print(f"🎥 Extracting audio from: {video_path}")
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path, codec="aac")
    print(f"🎵 Audio saved: {audio_path}")

def process_media_files():
    """Scans the folder, extracts/transcribes media files."""
    for file in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, file)

        if os.path.isfile(file_path):  # ✅ Ensure it's a file before processing
            file_name, file_ext = os.path.splitext(file)

            output_text_path = os.path.join(OUTPUT_FOLDER, f"{file_name}.txt")
            output_json_path = os.path.join(OUTPUT_FOLDER, f"{file_name}.json")

            # Check if it's an audio file
            if file_ext.lower() in AUDIO_EXTENSIONS:
                transcribe_audio(file_path, output_text_path, output_json_path)

            # Check if it's a video file
            elif file_ext.lower() in VIDEO_EXTENSIONS:
                audio_path = os.path.join(OUTPUT_FOLDER, f"{file_name}.m4a")

                # Extract audio & transcribe
                extract_audio(file_path, audio_path)
                transcribe_audio(audio_path, output_text_path, output_json_path)

if __name__ == "__main__":
    print("🚀 Starting Media Transcriber...")
    process_media_files()
    print("🎉 Done! Check your transcriptions in:", OUTPUT_FOLDER)
