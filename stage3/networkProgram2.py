import socket
# 一、client
#create a client
socket_client=socket.socket()
#connect to server
socket_client.connect(('192.168.43.111',8888))
while True:
    msg=input('you:')
    if msg=='exit':
        break
    socket_client.send(msg.encode('UTF-8'))
    recv_data=socket_client.recv(1024).decode()
    print(f'serve:{recv_data}')
socket_client.close()
