import networkx as nx
import matplotlib.pyplot as plt
from python_arptable import get_arp_table
import netifaces as ni
import os


class No_Grafo:
    def __init__(self, ip=1,hw=2):
        self.ip=ip
        self.hw=hw

    def __str__(self):
        return "IP="+str(self.ip)+" HW="+str(self.hw)

    def __repr__(self):
        return str(self.ip)
ip = ni.ifaddresses('enp5s0')
atrasos = []
arp = get_arp_table()
G = nx.Graph()
no = No_Grafo(ip[2][0]['addr'], ip[17][0]['addr'])
G.add_node(no)

for i in range(len(arp)):
    no = No_Grafo(arp[i]['IP address'], arp[i]['HW address'])
    G.add_node(no)
    lat = os.popen('ping -c 1 ' + arp[i]['IP address']).read()
    lat = float(lat.split('time=')[1].split('ms')[0])
    G.add_weighted_edges_from([(ip[2][0]['addr'], arp[i]['IP address'], lat)])
    atrasos.append(lat)

print(atrasos)

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()