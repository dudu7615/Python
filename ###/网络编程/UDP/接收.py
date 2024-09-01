from socket import *

ADDR = ("127.0.0.1",8080)
MY_ADDR = ("127.0.0.1",8081)

s = socket(AF_INET, SOCK_DGRAM)
s.bind(MY_ADDR)
s.sendto('你好'.encode("utf8"), ADDR)

reData = s.recvfrom(1024)
print(reData[0].decode("utf8"))