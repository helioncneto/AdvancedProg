import socket
import requests
import json
import os


def adoption(iface, ip_sw, ip_novo, mask, gw):
    ip = ip_sw.split('.')
    serv = ip[0]+'.' + ip[1] + '.' + ip[2] + '.1'
    #os.system('ifconfig ' + iface + ' down')
    #os.system('ifconfig ' + iface + ' hw ether 00:30:a7:17:f5:1f')
    #os.system('ifconfig ' + iface + ' ' + serv + '/16 up')
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (ip_sw, 3002)
    msg = '{"DefaultGateway":"' + gw + '","InterfaceSettings":[{"Address":{"FullAddress":"' + ip_novo + '/' + str(mask) + '"},"InterfaceId":"ETH_F"},{"Address":{"FullAddress":"' + ip_sw + '/16"},"InterfaceId":"ETH_MGMT"}]}'
    udp.connect(dest)
    udp.send(msg.encode())
    udp.close()
    payload = open('adopt.json', 'r')
    payload = json.load(payload)

    r = requests.post('https://' + ip_novo + ':443/api/default/security/Commission', json=payload, verify=False)
    print(r.text)


adoption('enp5s0', '169.254.61.63', '172.16.10.100', 24, '172.16.10.1')
