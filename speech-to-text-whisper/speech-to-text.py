# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
from pydub import AudioSegment
from pydub.utils import which
from dotenv import load_dotenv
import os

load_dotenv()

AudioSegment.converter = which("ffmpeg")
openai.api_key = os.environ.get("OPENAI_KEY")
interviewees = [{"name": "INTERVIEWEE", "language": 'da'}]

for interviewee in interviewees:
    print("Started with " + interviewee['name'])

    interview_audio = interviewee['name'] + "-optimized.m4a"

    # Create transcription
    audio_file= open("./../" + interview_audio, "rb")
    transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file, language=interviewee['language'])

    # Save file
    transcript_filename = 'transcriptions/' + interviewee['name'] + ".txt"
    with open(transcript_filename, "w") as file:
        file.write(transcript.text)

    print("Done with " + interviewee['name'])
