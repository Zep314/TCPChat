import socket
import threading

def read_sok():
    while 1 :
        data = sor.recv(1024)
        print(data.decode('utf-8'))

server = '127.0.0.1', 50505  # Данные сервера
alias = input("Input your alias: ") # Вводим наш псевдоним
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0)) # Задаем сокет как клиент
sor.sendto((alias+' Connect to server').encode('utf-8'), server)# Уведомляем сервер о подключении
t = threading.Thread(target= read_sok)
t.start()
while 1 :
    mensahe = input()
    if mensahe == 'quit':
        break
    sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)
print('Bye!')
