# Transcribing an interview

I am using [Whisper](https://openai.com/research/whisper) from OpenAI using python. [Here](https://platform.openai.com/docs/guides/speech-to-text) is a bit of documentation

Whisper can only take files that are maximum 25 mb. Therefore i am optimizing the audio files using this command: `ffmpeg -i allan.m4a -b:a 50k allan-optimized.m4a
`. Remember to install `ffmpeg`using `brew install ffmpeg`

Find openai key in the settings page of openai

Shit det kunne være fedt at i sin transkribering at have hvem der snakker. Der er nogle der har prøvet her, men det er nok lige i overkanten: https://github.com/openai/whisper/discussions/264

https://github.com/lablab-ai/Whisper-transcription_and_diarization-speaker-identification-

https://www.youtube.com/watch?v=MVW746z8y_I
