from Maquina import Maquina
import sys

#mensagens 
valida = "\nRepresentacao MTU valida\n"
invalida = "\nRepresentacao MTU invalida\n"

#funcao main efetua verificacoes no arquivo e na representacao que contem no arquivo
if __name__ == '__main__':

	try:
		arquivo = open( sys.argv[1] , 'r' ) 
	except:
		print("Erro ao abrir arquivo")	

	# R(M)w , onde R(m) e a representacao e w a palavra de entrada
	rMw = arquivo.read() 

	#verifica se a representacao e valida
	if rMw[:3] == "000": #comeca com 3 0s

		rMw = rMw[3:]
		segOcorrencia = rMw.find("000") #termina com 3 0s
		
		#nao encontrou a segunda ocorrencia é uma representacao invalida
		if segOcorrencia == -1:
			print ( invalida )
			exit(0)
		else:
			rM = rMw[:segOcorrencia]
			rM = rM.split("00") #separa a R(M) em uma lista em que cada posicao e a representacao de uma transicao

			if len( rM ) == 1: #nao conseguiu splitar
				print( invalida )
				exit(0)

			w = rMw[segOcorrencia+3:] # w esta depois da segunda ocorrencia de 3 0s

			terOcorrencia = w.find("000") # busca pelos ultimos 3 0s

			if terOcorrencia == -1: #nao encontrou os ultimos 3 0s, representacao invalida
				print ( invalida )
				exit(0)
			else:
				#retirnado os 3 ultimos 0s
				w = w[:len(w)-4]
				# lista contendo substrings da palavra w
				w = w.split('0')
				
				#adicionando B (branco) ao fim da palvra
				w.append('111')

				print ( valida )

				#executa a maquina com transicoes rM na palavra w 
				Maquina( rM , w ).executarMaquina()
	else:	
		print (invalida)
			
			

		




