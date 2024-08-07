from plyer import notification
import time
import winsound

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Lembrete de Pausa',
        timeout=10  # duração da notificação em segundos
    )
    # Tocar um som de notificação
    winsound.Beep(1000, 1000)  # Beep com frequência de 1000 Hz e duração de 1000 ms (1 segundo)

if __name__ == "__main__":
    while True:
        #Notificação para iniciar o trabalho / estudo
        show_notification('Tempo de Trabalho', 'Trabalhe / Estude por 25 minutos.')
        # Esperar 25 minutos (1500 segundos)
        time.sleep(1500)
        
        # Mostrar notificação para pausa
        show_notification('Tempo de Pausa', 'Descanse por 5 minutos.')
        # Esperar 5 minutos (300 segundos)
        time.sleep(300)
