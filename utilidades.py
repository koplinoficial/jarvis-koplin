from datetime import datetime

def hora_atual():
    agora = datetime.now()
    hora = agora.hour
    minuto = agora.minute

    if minuto == 0:
        return f"{hora} horas."
    
    return f"{hora} horas e {minuto} minutos."