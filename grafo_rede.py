import networkx as nx
import matplotlib.pyplot as plt
from python_arptable import get_arp_table
import netifaces as ni
import os
import paramiko

class SSH:
    def __init__(self, hostname, username, password, port):
        self.ssh = paramiko.SSHClient()
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=hostname, username=username, password=password, port=port)

    def exec_cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            return stderr
        else:
            return stdout


#iface = input("Digite sua interface de rede: ")
#ip = ni.ifaddresses(iface)
ip = ni.ifaddresses('wlp3s0')
arp = get_arp_table()
G = nx.Graph()
atributos = {0: {'IP': ip[2][0]['addr'], 'MAC': ip[17][0]['addr']}}
G.add_node(0)

for i in range(1, len(arp) + 1):
    atributos[i] = {'IP': arp[i-1]['IP address'], 'MAC': arp[i-1]['HW address']}
    G.add_node(i)
    lat = os.popen('ping -c 1 ' + arp[i-1]['IP address']).read()
    lat = float(lat.split('time=')[1].split('ms')[0])
    G.add_weighted_edges_from([(0, i, lat)])

nx.set_node_attributes(G, atributos)
nx.draw(G, with_labels=True, font_weight='bold')

for i in range(1, len(G.nodes)+1):
    ssh = SSH(G.nodes[i]['IP'], 'labcd', 'labcd', 22)
    for j in range(1, len(G.nodes)+1):
        ssh_lat = ssh.exec_cmd(['ping -c 1 ' + G.nodes[j]['IP']])
        ssh_lat = float(ssh_lat.split('time=')[1].split('ms')[0])
        G.add_weighted_edges_from([(i, j, ssh_lat)])

#plt.show()