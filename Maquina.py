import time

class Maquina():

	def __str__(self):
		out = ""
		out += ("FITA 1 [REGRAS]:\n" + str(self.fita1) + "\n\nFITA 2 [ESTADO_ATUAL]:\n" + str(self.fita2) 
			+ "\n\nFITA 3 [PALAVRA]:\n" + str(self.fita3) + "\n\n")
		return out

	def __init__(self, regras, palavra):
		self.fita1 = regras
		self.fita2 = "1" # estado inicial
		self.fita3 = palavra
		self.lista_transicoes = [Transicao(tran) for tran in regras]		
		self.cabesss_maquina = 0
		self.D = "1"
		self.E = "11"
		self.REJEITA = "\nPalavra rejeitada!!\n"
		self.ACEITA = "\nPalavra aceita!!\n"


	def buscarTransicao(self):
		estado_atual = self.fita2

		#cria uma lista com todas transicoes que existem partindo do estado atual
		transicoes = [transicao for transicao in self.lista_transicoes if transicao.estado_inicial == estado_atual]
		
		#se nao tiver transicoes a lista sera vazia
		if transicoes == []:
			return False
		
		for transicao in transicoes:
			if transicao.simbolo_entrada == self.fita3[self.cabesss_maquina]:
				try:
					self.executarTransicao(transicao)
					return True
				except ErroMaquina:
					print(self.REJEITA)
					exit(0)
		
		print(self.REJEITA)
		exit(0)


	def executarTransicao(self, transicao):

		self.fita2 = transicao.estado_destino
		self.fita3[self.cabesss_maquina] = transicao.simbolo_escrita
		if transicao.direcao == self.D:
			self.cabesss_maquina += 1
		else:
			self.cabesss_maquina -= 1
			if self.cabesss_maquina < 0:
				raise ErroMaquina 

	def executarMaquina(self):
		print("INICIO :")
		print(self )
		i = 1
		while self.buscarTransicao():
			## HEURISTICA
			print("Passo " + str(i) )
			print(self)	
			i+=1
			pass
		print(self.ACEITA)


class Transicao():

	def __init__(self, transicao_string):
		self.transicao_string = transicao_string.split('0')
		self.estado_inicial = self.transicao_string[0]
		self.simbolo_entrada = self.transicao_string[1]
		self.estado_destino = self.transicao_string[2]
		self.simbolo_escrita = self.transicao_string[3]
		self.direcao = self.transicao_string[4]

	def __str__(self):
		traducao_estado = lambda s: "q"+str(len(s)-1)
		dire = {
			"1" : "R",
			"11" : "L"
		}
		out = ""
		out += "[" + traducao_estado(self.estado_inicial) + ", " + self.simbolo_entrada + "] ->  "
		out += "[" + traducao_estado(self.estado_destino) + ", " + self.simbolo_escrita + ", " + dire[self.direcao] + "]\n"
		return out

class ErroMaquina(Exception):
	pass
