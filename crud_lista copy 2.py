import os 
os.system("cls || clear")

#CRUD usando listas 
#Creat = criar/ salvar
#Read = buscar/ selecionar
#Update = atualizar/ modificar
#Delete = apagar/ remover

#Criando a lista  de clientes 

lista_clientes = []

while True:                 #laço de repetição para  o usuario escolher a ação
    print("MENU DE OPÇÕES:")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Atualizar cliente")
    print("4 - Remover cliente")
    print("5 - Sair")
    escolha = input("Escolha uma opção (1-5): ")
    if escolha == '5':
        print("Saindo do programa.")
        break
    elif escolha == '1':
        nome = input("Digite o nome do cliente para adicionar: ")
        lista_clientes.append(nome)
        print(f"O cliente '{nome}' foi adicionado na lista.")
    elif escolha == '2':
        print("\nREAD - Listando os clientes da lista")
        if len(lista_clientes) == 0:
            print("Nenhum cliente na lista.")
        else:
            for i, cliente in enumerate(lista_clientes):
                print(f"{i} - {cliente}")
    elif escolha == '3':
        nome_atual = input("Digite o nome do cliente que deseja atualizar: ")
        if nome_atual in lista_clientes:
            nome_novo = input("Digite o novo nome: ")
            indice = lista_clientes.index(nome_atual)
            lista_clientes[indice] = nome_novo
            print(f"O cliente '{nome_atual}' foi atualizado para '{nome_novo}'.")
        else:
            print(f"O cliente '{nome_atual}' não foi encontrado na lista.")
    elif escolha == '4':
        nome_remover = input("Digite o nome do cliente que deseja remover: ")
        if nome_remover in lista_clientes:
            lista_clientes.remove(nome_remover)
            print(f"O cliente '{nome_remover}' foi removido da lista.")
        else:
            print(f"O cliente '{nome_remover}' não foi encontrado na lista.")
    
print("CREAT - Adicionando clientes na lista")
nome = "Maria"
lista_clientes.append(nome)
print(f"O cliente: {nome} foi adicionado na lista")

#Read - Lendo os clientes da lista
print("\nREAD - Listando os clientes da lista")
print(lista_clientes)

#Update - Atualizando um cliente na lista
print("\nUPDATE - Atualizando um cliente na lista")
nome_atualizado = "Maria"
if nome_atualizado in lista_clientes:
    nome_novo = "Maria Silva"
    indice = lista_clientes.index(nome_atualizado)
    lista_clientes[indice] = nome_novo
    print(f"O cliente: {nome_atualizado} foi atualizado para {nome_novo}")
else:
   print(f"O cliente: {nome_atualizado} não foi encontrado na lista") 
print(lista_clientes)

#Delete - Removendo um cliente da lista
print("\nDELETE - Removendo um cliente da lista")

nome_remover = "Maria"
if nome_remover in lista_clientes:
    lista_clientes.remove(nome_remover)
    print(f"O cliente: {nome_remover} foi removido da lista")
    
else:
    print(f"O cliente: {nome_remover} não foi encontrado na lista")

print(lista_clientes)