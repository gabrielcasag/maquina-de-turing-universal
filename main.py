from Maquina import Maquina
import sys

#mensagens 
valida = "\nRepresentacao MTU valida!!!\n"
invalida = "\nRepresentacao MTU invalida!!!\n"


if __name__ == '__main__':

	arquivo = open( sys.argv[1] , 'r' ) 

	rMw = arquivo.read() # R(M)w , onde R(m) e a representacao e w a palavra de entrada

	#verifica se a representacao e valida
	if rMw[:3] == "000": #comeca com 3 0s

		rMw = rMw[3:]
		segOcorrencia = rMw.find("000") #termina com 3 0s
		
		if segOcorrencia == -1:
			print ( invalida )
			exit(0)
		else:
			rM = rMw[:segOcorrencia]
			rM = rM.split("00")

			if len( rM ) == 1: #nao conseguiu splitar
				print( invalida )
				exit(0)

			w = rMw[segOcorrencia+3:] # w esta depois da segunda ocorrencia de 3 0s

			terOcorrencia = w.find("000")

			if terOcorrencia == -1: #nao encontrou 3 0s 
				print ( invalida )
				exit(0)
			else:
				#retirnado os 3 ultimos 0s
				w = w[:len(w)-4]
				# lista contendo substrings da palavra 
				w = w.split('0')
				
				#adicionando B (branco) ao fim da palvra
				w.append('111')

				print (valida )

				Maquina( rM , w ).executarMaquina()
	else:	
		print (invalida)
			
			

		




