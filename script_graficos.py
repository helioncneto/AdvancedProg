# encoding: utf-8
# -*- coding: cp1252 -*-.
#!/usr/bin/python

#whoami --> retorna o nome do usuário

import os
import matplotlib.pyplot as plt

def origem_destino_file():

	#Identificando os arquivos de saida do iperf
	files=os.listdir('files')
	iperf_results = {}
	temp=[]
	for file_name in files:
		if "saida" in file_name:
			temp[:]= file_name.split("-")
			key= str(temp[1]+'-'+temp[2])
			if key not in iperf_results:
				iperf_results[key]=[file_name]
			else:
				iperf_results[key].append(file_name) #colocar como atributo da classe
	#Abrindo os arquivos de saida do iperf e
	nomes=[]
	for o_d in iperf_results.keys():
		nome=o_d.split('-')
		nome="Origem:"+nome[0]+' Destino:'+nome[1]
		nomes.append(nome)
		arquivo1=open('files/'+nome,'w')
		for file_name in iperf_results[o_d]:
			temp=file_name.split('-')
			texto=temp[3].strip('M') #Taxa testada
			arquivo2=open('files/'+file_name,'r')
			linhas=arquivo2.readlines()
			server_report=False
			for linha in linhas:
				if "Server Report" in linha:
					server_report=True
					continue
				if server_report==True:
					linha=linha.split(' ')
					for i in range(len(linha)):
						if '/sec' in linha[i]:
							texto+=","+linha[i-1]
						if '%)' in linha[i]:
							texto+=","+linha[i].replace('%','').replace(')','').strip('(')
							arquivo1.write(texto)

	####FALTA CRIAR UMA FUNÇAO QUE JUNTE FAÇA A MEDIA DAS VAZOES

	''' #TENTATIVA FALHA POR ALGUM MOTIVO O SEGUNDO ARQUIVO ESTA APARECENDO COMO NULO
	for nome in nomes:
		arquivo=open(nome,'r')
		arquivo=arquivo.readlines()
		print arquivo 
		taxas=[]
		perdas=[]
		vazoes=[]
		for linha in arquivo:
			linha=linha.strip('\n')
			linha=linha.split(',')
			if linha[0] not in taxas:
				taxas.append(linha[0])
				vazoes.append(linha[1])
				perdas.append(linha[2])
			else:

				for i in range(len(taxas)):
					if linha[0]==taxas[i]:
						vazoes[i]=float(vazoes[i])+float(linha[1])
						perdas[i]=float(perdas[i])+float(linha[2])
		print vazoes
		print perdas
		arquivo2=open(nome,'w')
		for i in range(len(taxas)):
			arquivo2.write(str(taxas[i])+','+str(vazoes[i]/3)+','+str(perdas[i]/3)+'\n')
		arquivo2.close()

'''
def criar_graficos():
		files=os.listdir('.')
		par_origem_destino={}
		for file_name in files:
			if "Origem" in file_name:
				arquivo=open('files/'+file_name,'r')
				arquivo=arquivo.readlines()
				par_origem_destino[file_name]={}.fromkeys(["Taxas","Vazao","Perda"],[])
				for linha in arquivo:
					linha=linha.strip('\n')
					linha=linha.split(',')
					par_origem_destino[file_name]["Taxas"]=par_origem_destino[file_name]["Taxas"]+[float(linha[0])]
					par_origem_destino[file_name]["Vazao"]=par_origem_destino[file_name]["Vazao"]+[float(linha[1])]
					par_origem_destino[file_name]["Perda"]=par_origem_destino[file_name]["Perda"]+[float(linha[2])]
		#print par_origem_destino
		f=plt.figure(1)
		file_name=par_origem_destino.keys()
		#plt.scatter(par_origem_destino[file_name[0]]['Taxas'],par_origem_destino[file_name[0]]['Vazao'], par_origem_destino[file_name[1]]['Taxas'],par_origem_destino[file_name[1]]['Vazao'])
		plt.plot( par_origem_destino[file_name[0]]['Taxas'],par_origem_destino[file_name[0]]['Vazao'],'b-o', par_origem_destino[file_name[1]]['Taxas'],par_origem_destino[file_name[1]]['Vazao'],'r-*')
		#plt.plot( par_origem_destino[file_name[0]]['Taxas'],par_origem_destino[file_name[0]]['Vazao'],'b-o')
		plt.xlabel(u'Taxas Testadas (Mbps)')
		plt.ylabel(u'Médias das Vazões (Mbps)')
		plt.legend(file_name)
		plt.show()
		#f.savefig("Taxa_x_Vazao.pdf",bbox_inches='tight')

if __name__=='__main__':
	origem_destino_file()
	criar_graficos()