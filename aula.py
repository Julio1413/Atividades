import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}")
    print(f" - ID: {voice.id}")
    print(f" - Languages: {voice.languages}")
    