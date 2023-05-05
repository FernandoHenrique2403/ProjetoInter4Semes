#Criaçao do while para iniciar o sistema
escolha1 = input("Deseja iniciar o Sistema? (Sim ou Nao) ")

#while para prevernir que o usuario digite informaçoes erradas
while(escolha1!='sim' and escolha1!='Sim' and escolha1!='nao' and escolha1!='Nao'):
    print("Opcao invalida")
    escolha1 = input("Deseja iniciar o Sistema? (Sim ou Nao) ")
#caso usuario nao queira iniciar o sistema
while(escolha1=='nao' or escolha1=='Nao'):
    print("Encerrando o Sistema")
    break

#caso usuario escolha sim o sistema é iniciado
while(escolha1 == 'sim' or escolha1=='Sim'):
    #É feita a segunda pergunta dando as opções para o usuario do que deseja fazer 
    escolha2 = int(input("*"*56+"\n"+"*"*15+" PROJETO INTERDISCIPLINAR "+"*"*15+"\n"+"*"*56+"\nSelecione uma das opções abaixo:\n1-Calculadora\n2-Dados do Integrante\n3-Fechar o programa\n"+"*"*56+"\n"))

    if(escolha2 == 1):
        #Escolhendo a primeira opção entramos nos calculos do sistema e é feita a pergunta de qual seria a conversão e solicitação do numero que iremos converter
        escolha3 = int(input("Digite como será a conversão : \n1-Decimal => Binário\n2-Decimal => Hexadecimal \n3-Decimal => Octadecimal "))
        numero = int(input("Digite o numero que iremos converter: "))
        if(escolha3 == 1):
            binario = ""
            while numero > 0:
                resto = numero % 2
                binario += str(resto)
                numero //= 2
            binario = binario[::-1]
            print("O número binário é:", binario)
            escolha1 = input("Deseja continuar?")
        elif(escolha3 == 2):
            hexadecimal = ""
            while numero > 0:
                resto = numero % 16
                if resto < 10:
                    hexadecimal += str(resto)
                else:
                    hexadecimal += chr(ord('A') + resto - 10)
                numero //= 16
            hexadecimal = hexadecimal[::-1]
            print("O número hexadecimal é:", hexadecimal)
            escolha1 = input("Deseja continuar?")
        elif(escolha3 == 3):
            octal = ""
            while numero> 0:
                resto = numero % 8
                octal += str(resto)
                numero //= 8
            octal = octal[::-1]
            print("O número octal é:", octal)
            escolha1 = input("Deseja continuar?")
        else:
            #caso algum numero seja digitado fora do esperado é dada a mensagem de opção invalida
            print("Opcao invalida")
            escolha1 = input("Deseja Continuar?")

    if(escolha2 == 2):
        #Caso usuario solicite as informações do Integrante sera exibida a mensagem abaixo
        print("*"*56+"\nInformações do Integrante:\nCurso: Análise e Desenvolvimento de Sistemas\nIntegrante: Fernando Henrique dos Santos - RGM: 28232437\nMatérias envolvidas: Programação de Computadores e Organização e Arquitetura de Computadores\nVersão : 2.0 \n"+"*"*56)
        escolha1 = input("Deseja Continuar?")
    
    if(escolha2 == 3):
       #Caso seja escolhida a opção de encerrar o programa ele exibe a mensagem de encerramento e finaliza
       print("Encerrando o Sistema")
       break

    elif(escolha2<=0 or escolha2>=4):
        #caso o usuario digite algo fora do esperado no menu de opções ele é inforado da opção invalida e perguntado novamente se deseja continuar
        print("Opcao invalida")
        escolha1 = input("Deseja continuar?")
