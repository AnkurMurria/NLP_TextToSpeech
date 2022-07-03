from gtts import gTTS
import base64
import os


def convert(data):
    my_text = data
    tts = gTTS(text=my_text, lang='en', slow=False)
    path = os.path.join("convertedtext","converted-file.mp3")
    tts.save(path)  # save file as ... (here saving as mp3)
    with open(path, "rb") as file:
        my_string = base64.b64encode(file.read())
    return my_string
