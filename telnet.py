import telnetlib
from time import sleep

# Definindo Usuário e Senha
usuario = 'teste'
senha = 'teste'
Host = 'localhost'

class Telnet:
    def __init__(self, usuario, senha, host):
        self.tn = telnetlib.Telnet(host)
        #self.tn.set_debuglevel(100)
        # Enviando Usuário e Senha (Estabelecendo a Conexão)
        self.tn.read_until(b'midiacom-taesa login:', 5)
        self.tn.write(usuario.encode('ascii') + b"\n")
        self.tn.read_until(b'Password:', 5)
        self.tn.write(senha.encode('ascii') + b"\n")
        sleep(2)

    def enviar(self, cmd):
        # Enviando os Comandos
        self.tn.write(cmd.encode('ascii') + b"\n")

    def imprimir_tudo(self):
        self.tn.write(b"exit\n")
        print(self.tn.read_all().decode('utf-8'))



if __name__ == '__main__':
    t = Telnet(usuario, senha, Host)
    t.enviar('cat /etc/passwd')
    t.imprimir_tudo()



