from socket import socket,AF_INET,SOCK_DGRAM

MY_ADDR = ("127.0.0.1",8080)

udpSock = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字 
udpSock.bind(MY_ADDR)  # 绑定地址
while True:
    recvData = udpSock.recvfrom(1024)  # 接收数据
    udpSock.sendto(recvData[0], recvData[1])  # 发送数据