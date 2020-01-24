import socket
import struct
from fcntl import ioctl

#Constantes para por a interface em modo promiscuo
SOL_PACKET = 263
PACKET_ADD_MEMBERSHIP  = 1
PACKET_MR_PROMISC      = 1
SIOCGIFINDEX   = 0x8933

def get_if(iff,cmd):
    sck=socket.socket()
    ifreq = ioctl(sck, cmd, struct.pack("16s16x",iff))
    sck.close()
    return ifreq

#Poe a interface em modo promiscuo
IF_INDEX = int(struct.unpack("I",get_if("enp5s0", SIOCGIFINDEX)[16:20])[0])
mreq = struct.pack("IHH8s", IF_INDEX, PACKET_MR_PROMISC, 0, "")

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x88cc))
s.bind(("enp5s0", 0))
s.setsockopt(SOL_PACKET, PACKET_ADD_MEMBERSHIP, mreq)

def parse_ip(ip):
    lst = ip.split('.')
    novo = ''
    for i in range(len(lst[3])):
        if lst[3][i] in '0123456789':
            novo = novo + lst[3][i]
    lst[3] = novo
    ip = lst[0] + '.' + lst[1] + '.' + lst[2] + '.' + lst[3]
    return ip

while True:
    raw_data, addr = s.recvfrom(65536)

    split = raw_data.split('DATAPATH_ID:')
    datapath_id = split[1][:16]

    split = raw_data.split('ETH_FRONT_IP:')
    ip = split[1][:15]
    ip = parse_ip(ip)

    split = raw_data.split('ETH_REAR_IP:')
    manage_ip = split[1][:15]
    manage_ip = parse_ip(manage_ip)

