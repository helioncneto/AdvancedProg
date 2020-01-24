import socket
import struct
from fcntl import ioctl

SOL_PACKET = 263
PACKET_ADD_MEMBERSHIP  = 1
PACKET_MR_PROMISC      = 1
SIOCGIFINDEX   = 0x8933

def get_if(iff,cmd):
    sck=socket.socket()
    ifreq = ioctl(sck, cmd, struct.pack("16s16x",iff))
    sck.close()
    return ifreq

IF_INDEX = int(struct.unpack("I",get_if("enp5s0", SIOCGIFINDEX)[16:20])[0])

mreq = struct.pack("IHH8s", IF_INDEX, PACKET_MR_PROMISC, 0, "")

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x88cc))
s.bind(("enp5s0", 0))
s.setsockopt(SOL_PACKET, PACKET_ADD_MEMBERSHIP, mreq)

while True:
    raw_data, addr = s.recvfrom(65536)
    print(raw_data[139:155].decode())