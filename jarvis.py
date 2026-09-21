from comandos import abrir_chrome, abrir_vscode

import speech_recognition as sr
import pyttsx3
# Inicializa o sistema de voz

#variavel voz
voz = pyttsx3.init()

voz.setProperty("rate", 175)
voz.setProperty("volume", 1.0)

reconhecimento_de_voz = sr.Recognizer()

#função para entender comando de voz
def falar(texto):
    print(f"JARVIS: {texto}")
    voz.say(texto)
    voz.runAndWait()

def ouvir():
    with sr.Microphone() as source:
        print("\n= Estou ouvindo...")
        reconhecimento_de_voz.adjust_for_ambient_noise(source, duration=1)

        audio = reconhecimento_de_voz.listen(source)

    try:
        texto = reconhecimento_de_voz.recognize_google(audio, language= "pt-BR")
        print(f"VOCê {texto}")
        return texto.lower()

    except sr.UnknownValueError:
        print("JARVIS: Não consegui entender")
        return ""

    except sr.RequestError:
        print("JARVIS: Não consegui acesar o serviço de reconhecimento")
        return"" 

def executar_comando(comando):

    print(f"DEBUG - comando recebido: [{comando}]")
    if "chrome" in comando:
        falar("Abrindo Google Chrome.")
        abrir_chrome()

    elif "vs code" in comando or "visual studio code" in comando:
        falar("Abrindo Visual Studio Code.")
        abrir_vscode()

    else:
        falar("Ainda não conheço este comando.")
        
    
    #saida no prompt
print("=" * 50)
print("             KOPLIN JARVIS")
print("=" * 50)

falar("Sistemas online. Estou ouvindo.")

while True:

    comando = ouvir()

    if not comando:
        continue
    if "encerrar" in  comando or "desligar jarvis" in comando:
        falar("Encerrando sistema")
        break

    executar_comando(comando)
    

