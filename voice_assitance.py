import openai
import pyttsx3
import speech_recogniyion as sr
import time

openai.api_key="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"

engin = pyttsx3.init()

def spech_to_voice(filename):
    recogniz = sr.Recogniz()
    with sr.Audio_file(filename) as  source:
        audio = recogniz.record(source)
    try:
        return  recogniz.record_google(audio)
    except:
        print("skipping unknown error")

def generate_responce(prompt):
    response = openai.Completion.create(
        engine= "text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n = 1
        stop = None,
        temperature = 0.5,
    )
    return response["choice"][0]["text"]

def speak_text(text):
    engin.say(text)
    engin.runAndWait()

def main():
    while True:
        print("say welcome,to start recording any qwestion")
        with sr.Microphone() as source:
            recogniz = sr.Recogniz()
            audio = recogniz.listen(source)
            try:
                transcription = recogniz.recogniz_google(audio)
                if transcription.lower() == "welcome":

                    filename = "input.wav"
                    print("your question")
                    with sr.Microphone() as source:
                        recogniz = sr.Recogniz()
                        audio = recogniz.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "web") as f:
                            f.write(audio.get_wav_data())

                    text = audio_to_text(filename)
                    if text:
                        print(f"you said:,{text}")

                        response = generate_responce(text)
                        print(f"AI says:{response}")

                        speak_text(response)
            except Exception as e :
                print("an error occoured: {}".format{e})

if __name__ =="__main__":
    main()

