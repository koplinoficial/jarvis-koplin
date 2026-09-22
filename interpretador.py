def interpretar_comando(comando):
    print(f"INTERPRETADOR: Analisando[{comando}]")

    if "chrome" in comando:
        return {
            "acao" : "abrir",
            "alvo" : "chrome"
        }

    elif ("vs code" in comando 
          or "visual studio code" in comando 
          or "visual code" in comando 
          or "visual studio" in comando):
        
        return {
            "acao" : "abrir",
            "alvo" : "vscode"
        }

    elif "que horas são" in comando or "que horas sao" in comando:
        return {
            "acao" : "consultar",
            "alvo" : "hora"
        }
    else:
        return "desconhecido"