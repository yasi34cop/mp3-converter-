Extract MP3 from MP4 Video with FFmpeg in Python 🎵

Easily extract audio from a video file using FFmpeg with Python!

First, install the necessary module:
pip install ffmpeg-python

Then, use this script:
import ffmpeg

# https://t.me/LearnPython3

input_file = 'input.mp4'
output_file = 'output.mp3'

# Extract audio from the video
ffmpeg.input(input_file).output(output_file, format='mp3').run()

print('Audio extracted successfully!')

With ffmpeg-python, you can extract high-quality audio from your video files effortlessly.

📱 Join @LearnPython3 for more Python tips
