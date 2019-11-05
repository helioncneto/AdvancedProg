# encoding: utf-8
# -*- coding: cp1252 -*-.
# !/usr/bin/python
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


class IPERF:
    def __init__(self, config):
        self.config = config
        self.repeticoes, self.origens, self.destinos, self.taxas, self.portas = [], [], [], [], []

    def read_config(self):

        config_file = open(self.config, 'r')
        configurations = config_file.readlines()
        for line in configurations:
            line = line.split('=')
            if 'repetições' in line:
                self.repeticoes = line[1].strip('\n').split(',')
                for i in range(len(self.repeticoes)):
                    self.repeticoes[i] = self.repeticoes[i].strip(' ')

            elif 'origem' in line:
                self.origens = line[1].strip('\n').split(',')
                for i in range(len(self.origens)):
                    self.origens[i] = self.origens[i].strip(' ')

            elif 'destino' in line:
                self.destinos = line[1].strip('\n').split(',')
                for i in range(len(self.destinos)):
                    self.destinos[i] = self.destinos[i].strip(' ')

            elif 'taxas' in line:
                self.taxas = line[1].strip('\n').split(',')
                for i in range(len(self.taxas)):
                    self.taxas[i] = self.taxas[i].strip(' ')

            elif 'portas' in line:
                self.portas = line[1].strip('\n').split(',')
                for i in range(len(self.portas)):
                    self.portas[i] = self.portas[i].strip(' ')
        self.call_iperf(self.repeticoes, self.origens, self.destinos, self.taxas, self.portas)

    def call_iperf(self, repeticoes, origens, destinos, taxas, portas):
        for r in range(int(repeticoes[0])):
            for od in range(len(origens)):
                for t in range(len(taxas)):
                    ssh_d = SSH(destinos[od], 'labcd', 'labcd', 22)
                    out_d = ssh_d.exec_cmd('iperf -s -u -p 5003 &')

                    ssh_o = SSH(origens[od], 'labcd', 'labcd', 22)
                    out_o = ssh_o.exec_cmd('iperf -c ' + destinos[od] + ' -u -b ' + taxas[t] + ' -p 5003')
                    arq = open('saida-' + origens[od] + '-' + destinos[od] + '-' + taxas[t] + '-' + str(r), 'a')
                    for l in out_o.readlines():
                        arq.write(l)
                    arq.close()
                    out_d = ssh_d.exec_cmd('killall -15 iperf')


if __name__ == '__main__':
    obj = IPERF('config.txt')
    obj.read_config()