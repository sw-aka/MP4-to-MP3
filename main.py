import os
from pydub import AudioSegment

# Define input and output directories
INPUT_DIRECTORY = 'INPUT_VIDEOS'
OUTPUT_DIRECTORY = 'OUTPUT_AUDIO'

# Attempt to list files in the input directory
try:
    input_file_names = os.listdir(INPUT_DIRECTORY)
except FileNotFoundError as exc:
    raise FileNotFoundError(f"Input directory '{INPUT_DIRECTORY}' not found.") from exc

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

# Process each file in the input directory
for file_name in input_file_names:
    # Construct full file paths for input and output
    input_video = os.path.join(INPUT_DIRECTORY, file_name)
    output_audio = os.path.join(OUTPUT_DIRECTORY, os.path.splitext(file_name)[0] + '.mp3')

    # Load the video file and extract audio
    audio = AudioSegment.from_file(input_video, format="mp4")
    
    # Export the extracted audio as an MP3 file
    audio.export(output_audio, format="mp3")

    # Print a message indicating successful extraction
    print(f"Audio extracted and saved as {output_audio}")

# Final message indicating completion of the process
print("Audio extraction completed successfully.")
