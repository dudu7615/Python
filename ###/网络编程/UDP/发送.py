from socket import *
import time
s = socket(AF_INET, SOCK_DGRAM)  # IPV4,UDP
for _ in range(10):
    time.sleep(1)
    s.sendto('你好'.encode("utf8"), ("127.0.0.1",8080))