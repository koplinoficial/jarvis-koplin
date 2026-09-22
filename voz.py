import speech_recognition as sr
import pyttsx3


reconhecimento_de_voz = sr.Recognizer()


def falar(texto):
    print(f"JARVIS: {texto}")

    voz = pyttsx3.init()
    voz.say(texto)
    voz.runAndWait()


def ouvir():
    with sr.Microphone() as source:
        print("\n= Estou ouvindo...")

        audio = reconhecimento_de_voz.listen(
            source,
            timeout=5,
            phrase_time_limit=5)

    try:
        texto = reconhecimento_de_voz.recognize_google(
            audio,
            language="pt-BR"
        )

        print(f"VOCÊ: {texto}")
        return texto.lower()

    except sr.UnknownValueError:
        print("JARVIS: Não consegui entender.")
        return ""

    except sr.RequestError:
        print("JARVIS: Não consegui acessar o serviço de reconhecimento.")
        return ""

def calibrar_microfone():
    with sr.Microphone() as source:
        print("JARVIS: Calibrando microfone...")
        reconhecimento_de_voz.adjust_for_ambient_noise(source, duration=1)
    print("JARVIS: Microfone calibrado.")