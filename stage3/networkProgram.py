# socket is responsible for transfering data
# between progress a and progress b
import socket
# 一、server
'''
# a.basic grammer
# 1.create a socket object 
socket_server=socket.socket()
socket_server.bind(('192.168.43.111',8888))
# listen the port.limit the numbers of connection
socket_server.listen(3)
# 2. wait for client and get connection object,accept()is Blocking functions
# return information of connection
result:tuple=socket_server.accept()
conn=result[0]     #connection object between server and client
address=result[1]  #information about client's address
print('accept a connection')
# 3.accept message
data=conn.recv(1024).decode('UTF-8')  #return byte so we need to decode
print(f'data from client: {data}')
# 4.send message
msg='server has receviced the message'.encode('UTF-8')
conn.send(msg)

# 3. close connection
conn.close()
'''

# b.update
# a.basic grammer
# 1.create a socket object
socket_server=socket.socket()
# check ipv4 address via ipconfig(cmd command)
socket_server.bind(('192.168.0.10',8888))
# listen the port.limit the numbers of connection
socket_server.listen(3)
# 2. wait for client and get connection object,accept()is Blocking functions
result:tuple=socket_server.accept()
conn=result[0]     #connection object between server and client
address=result[1]  #information about client's adress
print('accept a connection')
while True:
    data=conn.recv(1024).decode('UTF-8')  #return byte so we need to decode
    print(f'data from client: {data}')
    msg='server has receviced the message'.encode('UTF-8')
    if data=='exit':
        break
    conn.send(msg)
# 3. close connection
conn.close()