import json
import re
import conexao


# Função para verificar o login e a senha
def verificar_login_senha(email, senha):
    with open('clientes.json', 'r', encoding='utf-8') as f:
        clientes = json.load(f)
        for cliente in clientes:
            if cliente['email'] == email:
                if cliente['senha'] == senha:
                    return True, cliente['nome'], cliente['id']
                else:
                    return False, "Senha incorreta", None

        return False, "Usuário inexistente", None
    




#Veerifa se o cliente possui o produto
def verificaProduto(id):
    with open('clientes.json', 'r', encoding='utf-8') as f:
        clientes = json.load(f)
        for cliente in clientes:
            if cliente['id'] == id:
                if cliente['produto'] == True:
                    return True
                else:
                    return False




#Recebe dados do json e atualiza com novo cliente
def clientes_global(clientes, nome, email, cep, senha):
    try:
        with open('clientes.json', 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:  # Verifica se o conteúdo do arquivo está vazio
                clientes = []
            else:
                f.seek(0)  # Volta para o início do arquivo
                clientes = json.load(f)
    
    except FileNotFoundError:
        clientes = []

    cliente_id = f'cliente{len(clientes) + 1}'  # Gere um ID único
    cliente = {
        'id': cliente_id,
        'nome': nome,
        'email': email,
        'cep': cep,
        'senha': senha,
        'produto':False
    }
    clientes.append(cliente)

    with open('clientes.json', 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)





#Function para validar as informações obtidas do cliente
def validar_informacoes(nome, cep, email):
    if not re.match("^[a-zA-Z\s\w~]*$", nome, re.UNICODE):
        print("Nome só pode conter letras")
        return False
    if not re.match("^\d{5}-\d{3}$", cep):
        print("CEP deve ser composto de 5 dígitos, um traço e 3 dígitos")
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("O e-mail está inválido")
        return False
    return True





#Verifica o local da instalação
def validar_instalacao(end,tel,cpf):
    if not re.match(r'^[A-Za-z0-9\s,]*$', end):
        print("Endereço inválido... Insira os dados novamente\n")
        return False
    elif not re.match(r'^\d{5}-\d{4}$', tel) and not re.match(r'^\d{7}-\d{4}$', tel) and not re.match(r'^(\d{2})\d{5}-\d{4}$', tel):
        print("O telefone inserido deve ter no mínimo 9 dígitos (ou 11 com o DDD)... Insira os dados novamente\n")
        return False
    elif not re.match(r'^\d{9}-\d{2}$', cpf):
        print("CPF deve possuir 9 dígitos, um traço e 2 dígitos... Insira os dados novamente\n")
        return False
    else:
        print("---Informações da instalação recebidas com sucesso!---")
        return True
    



#Compra do produto
def option1(id):
    print("\n\n----- COMPRA DO CLEAN DRAIN -----")
    print("\n\nClaro,o preço de um Clean Drain com o custo de instalação é de R$120,00 com o frete grátis!")

    escolha = input("Deseja adquirir o seu agora mesmo? ('S' para confirmar) ").lower()
    if escolha == 's':
        print("Ótimo, para prosseguirmos precisamos de mais 3 informações: ")

        x = True
        while x == True:
            endereco = input("Insira o endereço da instalação: ")
            telefone = input("Insira o telefone do responsável que acompanhará a instalação ((xx)xxxxx-xxxx): ")
            cpf = input("Insira o cpf do responsável que acompanhará a instalação (xxxxxxxxx-xx): ")
            
            if validar_instalacao(endereco, telefone, cpf) is True:
                x = False

        #Passa as informações recebidas para uma tupla
        info_instalacao = (endereco, telefone, cpf)
        
        print("\nComo desejar realizar o pagamento?")
        pag = int(input("1-PIX\n2-Cartao de crédito/débito."))
        
        if pag == 1:
            print("\n\nBasta escanear o código ou enviar o valor para '(11) 951504504' ")
        else:
            print("\n\nPÁGINA DE PAGAMENTO COM CARTÃO VIA PAGSEGURO")
        
        print("Pagamento realizado com sucesso!")
        print("---- Resumo da Instalação: ----")
        print(f"O Clean Drain será instalado em: {info_instalacao[0]}")
        print(f"O telefone do responsável por acompanhar a instalação é: {info_instalacao[1]}")
        print(f"O CPF do responsável por acompanhar a instalação é: {info_instalacao[2]}")
        print("Obrigado por adquirir o Clean Drain conosco!\n")
        
        
        ### Atualiza no json que o cliente agora possui o produto
        cliente_produto = True

        with open('clientes.json', 'r', encoding='utf-8') as f:
            clientes = json.load(f)
            for cliente in clientes:
                if cliente['id'] == id:
                    cliente['produto'] = cliente_produto

        with open('clientes.json','w') as f:
            json.dump(clientes,f, indent=4, ensure_ascii=False)

        escolha2 = int(input("\nDeseja voltar ao menu principal (digite 1) ou fazer o Log-Out (digite 2)? "))

        if escolha2 == 1:
            menu = 1
        else:
            menu = 2

    else:
        print("Ok, sem problemas, agradecemos a sua visita!")
        menu = 2
    
    return menu




#Status do Clean Drain
def option2():
    print("\n\n----- STATUS DO CLEAN DRAIN -----")

    print("\n-- É recomendado remover o lixo por volta dos 5Kg e/ou quando está á 20cm do teto! --")

    vol, weight, data = conexao.conexao_Arduino() 

    print(f"\n\nO seu Clean Drain está com: \n- {weight} KG de lixo acumulado\n- {vol} centimetros do 'teto'.")
    print(f"Data e hora da última checagem: {data}") 
        
    if weight > 5 :
        print("\nALERTA! O peso do seu lixo ultrapassa os 5kg. Recomenda-se remover o lixo o mais rápido possível!")
    elif vol > 20:
        print("\nALERTA! O volume do seu lixo ultrapassa os 20cm do teto. Recomenda-se remover o lixo o mais rápido possível!")
    elif weight > 5 and vol > 20:
        print("\nALERTA! O peso e o volume do seu lixo ultrapassam os limites. Recomenda-se remover o lixo o mais rápido possível!")
    else:
        print("\nO volume e o peso do seu lixo estão abaixo do limite, ainda não é necessário removê-lo")

    escolha = int(input("\nDeseja voltar ao menu principal (digite 1) ou fazer o Log-Out (digite 2)? "))
        
    if escolha == 1:
        menu = 1
    else:
        menu = 2 
    
    return menu






#Manutenção do Clean Drain
def option3():
    print("\n\n----- MANUTENÇÃO DO CLEAN DRAIN -----")

    print("\n\nClaro,o preço da manutenção começa a partir de de R$30.00 mas pode variar caso haja necessidade de troca de peças! Como deseja efetuar o pagamento?")
    pag = int(input("1-PIX\n2-Cartao de crédito/débito."))
    if pag == 1:
        print("\n\nBasta escanear o código ou enviar o valor para '(11) 951504504' ")
    else:
        print("\n\nPÁGINA DE PAGAMENTO COM CARTÃO VIA PAGSEGURO")
    print("--- Pagamento realizado com sucesso! ---")
    
    escolha = int(input("\nDeseja voltar ao menu principal (digite 1) ou fazer o Log-Out (digite 2)? "))
    if escolha == 1:
        menu = 1
    else:
        menu = 2  
    
    return menu