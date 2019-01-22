import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_addr = ('11.11.11.11',6666)
s.bind(s_addr)
s.listen(10)


