import json
import re
import funcoes



clientes = []
menu = 0




while menu == 0:
    option = int(input("1- Deseja fazer o login? \n2- Deseja fazer o cadastro?\n"))

    if option == 1:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        acesso_permitido, nome_usuario, usuario_id = funcoes.verificar_login_senha(email, senha)

        if acesso_permitido:
            print(f"\nAcesso permitido! Bem-vindo, {nome_usuario}!\n")
            menu = 1
        else:
            print(f"\nAcesso negado: {nome_usuario}\n\n")
    
    elif option == 2:
        print("Bem-vindo! Por favor, faça o seu registro!\n")
        nome = input("Por favor, informe seu nome:\n ")
        email = input("Digite o e-mail:\n ")
        cep = input("Informe seu CEP (formato xxxxx-xxx):\n ")
        senha = input("Digite sua senha!\n")
        senha2 = input("Confirme sua senha!\n")

        #chama a function que valida as informações e faz as devidas checagens
        if funcoes.validar_informacoes(nome, cep, email):
            if senha != senha2 :
                print("Por favor, verifique as informações e tente novamente.")
            else:
                print("Informações válidas. Registro concluído!")
                print("Faça o login!\n\n")
                funcoes.clientes_global(clientes, nome, email, cep, senha)
                option = 1 #Abre o menu principal




#Menu principal
while menu == 1 :
    print(f"\n\n------Bem vindo a nossa Homepage {nome_usuario}!,Quais dos serviços disponiveis você deseja acessar------")
    
    #Se o usuário possuir o produto
    if funcoes.verificaProduto(usuario_id):

        option = int(input("\n\n1-Desejo verificar o status do meu Clean drain\n2-Desejo solicitar a manutenção do meu clean drain\n3-Desejo Fazer Log-Out do app\n"))

        if option == 1:
            menu = funcoes.option2()
        
        elif option == 2:
            menu = funcoes.option3()
        
        elif option == 3:
            menu = 2



    #Se o usuário não possuir o produto
    else:
        print("Não possui o produto")
    
        option = int(input("\n\n1-Desejo solicitar o meu Clean Drain!\n2-Desejo Fazer Log-Out do app\n"))
        
        #Solicitar Clean Drain
        if option == 1 :
            menu = funcoes.option1(usuario_id)
        
        else: 
            menu = 2
        
    #Log-out do programa
    if menu == 2:
            print("\nClaro! Adeus, espero que volte logo!:D")   
            break 
