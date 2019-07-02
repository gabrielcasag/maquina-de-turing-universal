# -*- coding: utf-8 -*-

#classe principal que representa a MTU
class Maquina():
	#descritor para visualizacao das fitas
	def __str__(self):
		out = ""
		out += ("FITA 1 [REGRAS]:\n" + str(self.fita1) + "\n\nFITA 2 [ESTADO_ATUAL]:\n" + str(self.fita2) 
			+ "\n\nFITA 3 [PALAVRA]:\n" + str(self.fita3) + "\n\n")
		return out
		
	def __init__(self, regras, palavra):
		self.fita1 = regras 	  #fita1 contem a lista de regras
		self.fita2 = "1"		  #fita2 contem o estado inicial
		self.fita3 = palavra      #fita3 contem a palavra
		self.lista_transicoes = [Transicao(tran) for tran in regras]		#lista de objetos transicao
		self.cabesss_maquina = 0  #controla a posicao da cabeca de leitura/escrita										
		self.D = "1"              #direcoes da maquina para facilitar implementacao
		self.E = "11"
		self.REJEITA = "\nPalavra rejeitada\n" #mensagens de saida
		self.ACEITA = "\nPalavra aceita\n"
		self.ultima_transicao = []             #ultima transicao , usado na heuristica

	#busca uma transicao e tenta executa-la
	def buscarTransicao(self):

		estado_atual = self.fita2

		#cria uma lista com todas transicoes que existem partindo do estado atual
		transicoes = [transicao for transicao in self.lista_transicoes if transicao.estado_inicial == estado_atual]
		
		#se nao tiver transicoes a lista sera vazia
		if transicoes == []:
			return False, self.ultima_transicao
		
		#para todas possiveis transicoes partindo do estado atual, executar a que convem
		for transicao in transicoes:
			if transicao.simbolo_entrada == self.fita3[self.cabesss_maquina]:
				try:
					self.ultima_transicao = transicao
					self.executarTransicao(transicao)
					return True, self.ultima_transicao
				except ErroMaquina:
					print(self.REJEITA)
					exit(0)
		
		print(self.REJEITA)
		exit(0)

	#realiza alteracoes nas fitas
	def executarTransicao(self, transicao):

		self.fita2 = transicao.estado_destino
		self.fita3[self.cabesss_maquina] = transicao.simbolo_escrita
		if transicao.direcao == self.D:
			self.cabesss_maquina += 1
		else:
			self.cabesss_maquina -= 1
			if self.cabesss_maquina < 0:
				raise ErroMaquina 

	#busca transicoes e implementa heuristicas
	def executarMaquina(self):
		print("INICIO :")
		print( self )
		#contador 
		i = 1
		#var é uma tupla contendo ( Bool , ultima_transicao ) que controla o loop
		var = self.buscarTransicao()
		#dicionario usado na heuristica
		conta_transicao = dict()
	
		while var[0] :
			## HEURISTICAS

			#se executar muitas vezes o tamanho da palavra pode ser um possivel loop infinito 
			#calculado pelo tamanho da palavra(fita3) elevado a quantidade de transicoes ( fita1 )
			#nunca encontra uma forma de alcançar um estado de aceitacao
			#falharia se a maquina for um processo de copiar uma grande quantidade de vezes uma palavra
			if i > (len( self.fita3 ) ** len( self.fita1 ) ):
				print(self.REJEITA)
				print("possivel loop infinito")
				exit(0)

		
			#se executar muitas vezes na mesma transiçao pode ser um possivel loop infinito
			#calculado pelo tamanho da palavra elevado a quantidade de transicoes
			#falharia no caso de ser uma maquina que reconhece ab^i com uma quantidade muito grande de b's
			try:
				conta_transicao[var[1]] +=1
			except KeyError:
				conta_transicao[var[1]] = 0

			maior_ocorrencia = max( conta_transicao , key = conta_transicao.get )

			if conta_transicao[maior_ocorrencia] == var[1] and maior_ocorrencia > ( len( self.fita3 ) ** len( self.fita1) ):
				print(self.REJEITA)
				print("possivel loop infinito")
				exit(0)

			print("Passo " + str(i) )
			print(self)	
			i+=1

			#busca a proxima transicao e retorna uma tuplaem var ( bool , ultima_transicao )

			var = self.buscarTransicao() #buscando proxima transicao
			
			pass
		

		print(self.ACEITA)

#classe para tradução das transicoes a fim de facilitar manipulacoes
class Transicao():

	def __init__(self, transicao_string):
		self.transicao_string = transicao_string.split('0')
		self.estado_inicial = self.transicao_string[0]
		self.simbolo_entrada = self.transicao_string[1]
		self.estado_destino = self.transicao_string[2]
		self.simbolo_escrita = self.transicao_string[3]
		self.direcao = self.transicao_string[4]
	#descritor da transicao para facilitar visualizacao
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
