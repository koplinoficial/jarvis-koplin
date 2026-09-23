import json


def carregar_memoria():
    with open("memoria.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_memoria(memoria):
    with open("memoria.json", "w", encoding="utf-8") as arquivo:
        json.dump(memoria, arquivo, indent=4, ensure_ascii=False)