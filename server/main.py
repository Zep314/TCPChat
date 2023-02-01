import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('127.0.0.1',50505))
clients = [] # Массив где храним адреса клиентов
print ('Start Server')
while 1 :
    data , addres = sock.recvfrom(1024)
    print (addres[0], addres[1])
    if  addres not in clients :
        clients.append(addres)# Если такого клиента нету , то добавить
        sock.sendto(b'Greeting!',clients[-1])
    for client in clients :
        if client == addres :
            continue # Не отправлять данные клиенту, который их прислал
        sock.sendto(data,client)

