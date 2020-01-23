import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x88cc))
# s.bind(("enp5s0", 0))

while True:
    raw_data, addr = s.recvfrom(65536)
    print(raw_data[128 + 11:128 + 11 + 16])