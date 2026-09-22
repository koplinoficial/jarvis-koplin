from comandos import abrir_chrome, abrir_vscode
from utilidades import hora_atual
from voz import falar, ouvir, calibrar_microfone
from interpretador import interpretar_comando


def executar_comando(comando):

    print(f"DEBUG - comando recebido: [{comando}]")

    comando_interpretado = interpretar_comando(comando)

    acao = comando_interpretado["acao"]
    alvo = comando_interpretado["alvo"]

    print(f"DEBUG - ação: [{acao}]")
    print(f"DEBUG - alvo: [{alvo}]")

    falar(f"Entendi: ação {acao}, alvo {alvo}.")
    
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
    

