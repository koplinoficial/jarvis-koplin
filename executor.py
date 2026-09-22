from comandos import abrir_chrome, abrir_vscode


def executar(intencao):

    acao = intencao["acao"]
    alvo = intencao["alvo"]

    if acao == "abrir":

        if alvo == "chrome":
            abrir_chrome()

        elif alvo == "vscode":
            abrir_vscode()

        else:
            print(f"EXECUTOR: Não sei abrir [{alvo}]")

    else:
        print(f"EXECUTOR: Não conheço a ação [{acao}]")