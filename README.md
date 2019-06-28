# maquina-de-turing-universal

Trabalho realizado para a discplina de Teoria da Computação , UFLA ;

- Implementação de Maquina de Turing Universal ( MTU ) que executa a partir de um arquivo texto
- Sua chamada se da por linha de comando, seguindo o padrão a seguir:
  
    __Python:__
      Python program.py __argumento1__

- __argumento1__ é	o	caminho	para	um arquivo	texto,	codificado	em	UTF-8,	que	contém	a representação	de	
  uma	máquina	de	Turing __M__ qualquer	__(R(M))__	seguida	de	uma	entrada __w__ .
  
- Arquivo texto contem uma representaçao binária de MTU R(M)w.
- 0s representam delimitadores da representaçao,
- 1s são uma representaçao unaria de cada componente da maquina,

- O programa imprime a cada passo da execução das transicões as _três fitas_ usadas na computação
  - Fita 1 contém as regras de transiço da maquina M
  - Fita 2 contém o estado atual da computação
  - Fita 3 contém a palavra __w__
- Ao final da execução uma mensagem é retornada dizendo se foi possível aceitar ou rejeitar a palavra, podendo entrar em loop infinito. 

