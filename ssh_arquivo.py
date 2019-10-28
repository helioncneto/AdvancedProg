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

def ler_arquivo(arquivo):
    configs = dict()
    f = open(arquivo, 'r')
    for l in f.readlines():
        linha = l.split('=')
        if linha[0] == 'Usuario':
            configs['usuarios'] = linha[1].split(',')
        elif linha[0] == 'Senha':
            configs['senhas'] = linha[1].split(',')
        elif linha[0] == 'Host':
            configs['hosts'] = linha[1].split(',')
        elif linha[0] == 'Porta':
            configs['portas'] = linha[1].split(',')
        elif linha[0] == 'Comando':
            configs['comandos'] = linha[1].split(',')
        elif linha[0] == 'Saida':
            configs['saida'] = linha[1]
    f.close()
    return configs

def executar(config):
    for i in range(len(config['hosts'])):
        host = config['hosts'][i].replace('\n','')
        user = config['usuarios'][i].replace('\n','')
        passwd = config['senhas'][i].replace('\n','')
        prt = int(config['portas'][i].replace('\n',''))
        comando = config['comandos'][i].replace('\n','')
        ssh = SSH(hostname=host, username=user, password=passwd, port=prt)
        saida = ssh.exec_cmd(comando)
        f = open(config['saida'], 'a')
        for l in saida.readlines():
            f.write(l)
        f.close()

if __name__ == '__main__':
    configs = ler_arquivo('config.ssh')
    executar(configs)