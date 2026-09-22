def interpretar_comando(comando):
    print(f"INTERPRETADOR: Analisando[{comando}]")

    if "chrome" in comando:
        return "abrir_chrome"

    elif ("vs code" in comando 
          or "visual studio code" in comando 
          or "visual code" in comando 
          or "visual studio" in comando):
        
        return "abrir_vscode"

    elif "que horas são" in comando or "que horas sao" in comando:
        return "hora_atual"
    else:
        return "desconhecido"