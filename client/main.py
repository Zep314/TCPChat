# Клиент для простого TCP чата

import socket
import threading

# Класс - поток, работающий на прием (пишет в консоль, все, что приходит от сервера)
class CustomThread(threading.Thread):
    def __init__(self, event):
        # call the parent constructor
        super(CustomThread, self).__init__()
        # store the event
        self.event = event

    def run(self):
        # Рабочий цикл потока, который работает на прием
        while True:
            if self.event.is_set():
                break
            data = sock.recv(1024)
            print(data.decode('utf-8'))

server = '127.0.0.1', 50505  # Подключаемся сюда
alias = input("Input your alias: ") # Вводим наш псевдоним
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(server)
sock.sendto(('[' + alias + ']Hello world!' ).encode('utf-8'), server) # Приветствие

event = threading.Event()
thread = CustomThread(event)
thread.start()
while True: # Рабочий цикл потока, который работает на отправку
    inp = input()
    if inp == 'quit':
        break
    sock.sendto(('[' + alias + ']' + inp).encode('utf-8'), server)

# Гасим принимающий поток
event.set()
thread.join()

print('Bye!')
