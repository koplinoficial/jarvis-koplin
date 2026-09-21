from comandos import abrir_chrome, abrir_vscode
from utilidades import hora_atual
from voz import falar, ouvir, calibrar_microfone

def executar_comando(comando):

    print(f"DEBUG - comando recebido: [{comando}]")

    if "que horas são" in comando or "que horas sao" in comando:
        hora = hora_atual()
        falar(f"Agora são{hora}.")
        return

    if "chrome" in comando:
        falar("Abrindo Google Chrome.")
        abrir_chrome()

    elif "vs code" in comando or "visual studio code" in comando or "vscode" in comando or "code" in comando:
        falar("Abrindo Visual Studio Code.")
        abrir_vscode()

    else:
        falar("Ainda não conheço este comando.")
        
    
    #saida no prompt
print("=" * 50)
print("             KOPLIN JARVIS")
print("=" * 50)

calibrar_microfone()

falar("Sistemas online. Estou ouvindo.")


while True:

    comando = ouvir()

    if not comando:
        continue
    if "encerrar" in  comando or "desligar jarvis" in comando:
        falar("Encerrando sistema")
        break

    executar_comando(comando)
    

