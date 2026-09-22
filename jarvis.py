from comandos import abrir_chrome, abrir_vscode
from utilidades import hora_atual
from voz import falar, ouvir, calibrar_microfone
from interpretador import interpretar_comando


def executar_comando(comando):

    print(f"DEBUG - comando recebido: [{comando}]")

    comando_interpretado = interpretar_comando(comando)

    if comando_interpretado == "hora_atual":
        hora = hora_atual()
        falar(f"Agora são {hora}.")
        return

    elif comando_interpretado == "abrir_chrome":
        falar("Abrindo Google Chrome.")
        abrir_chrome()

    elif comando_interpretado == "abrir_vscode":
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
    

