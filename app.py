import os
import openai
import requests
from datetime import datetime
import subprocess
import time
import speech_recognition as sr

# setting API key
openai.api_key = os.environ["SECRET_KEY"]
os.environ["DISPLAY"] = ":0"
identifier = ""

subprocess.Popen(f"feh -F title.png &", shell=True)

# waiting for wake word
def wake_word_detection():
    global identifier
    try:
        r = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            r.adjust_for_ambient_noise(source)

        print("Listening for wake word...")
        while True:
            with mic as source:
                audio = r.listen(source)
            try:
                text = r.recognize_google(audio).lower()
                print("Recognized Text:", text)
                
                # the default wake word and 3 example artist wake words 
                if "picture frame" in text.lower():
                    return "Pie"
                if "picasso" in text.lower():
                    print("Wake word detected!")
                    identifier = "in the style of Pablo Picasso, "
                    return "Pie"
                if "da vinci" in text.lower():
                    print("Wake word detected!")
                    identifier = "in the style of Leonardo da Vinci, "
                    return "Pie"
                if "van go" in text.lower():
                    print("Wake word detected!")
                    identifier = "in the style of Vincent van Gogh, "
                    return "Pie"
            except sr.UnknownValueError:
                pass
    except Exception as e:
        print(f"Error: {e}")
        return ""

# listening for prompt
def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your prompt...")
        try:
            subprocess.Popen(f"feh -F speak.png &", shell=True)
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except (sr.UnknownValueError, sr.RequestError) as e:
            print(f"Speech recognition error: {e}")
    return None

while True:
    wake_word_detection()
    PROMPT = record_audio()
    subprocess.Popen(f"feh -F generating.png &", shell=True)

    # image generation
    if PROMPT:
        response = openai.Image.create(
            prompt= identifier + PROMPT,
            model="dall-e-3",
            n=1,
            size="1792x1024",
        )

        url = response["data"][0]["url"]
        data = requests.get(url).content

        # naming created image
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = f'output/img{timestamp}.png'
        with open(file_name, 'wb') as f:
            f.write(data)

        # opening image
        print(f"Image saved as {file_name}")
        subprocess.Popen(f"feh -F {file_name} &", shell=True)
        time.sleep(2)

