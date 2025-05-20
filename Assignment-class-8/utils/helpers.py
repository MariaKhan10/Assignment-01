from gtts import gTTS
import os
import tempfile

def text_to_speech(text, lang_code="en", filename="temp_audio.mp3"):
    tts = gTTS(text=text, lang=lang_code)
    temp_dir = tempfile.gettempdir()  # This will use the correct tmp folder for your OS
    filepath = os.path.join(temp_dir, filename)
    tts.save(filepath)
    return filepath
