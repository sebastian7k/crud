import os 
os.system("cls || clear")

#CRUD usando listas 
#Creat = criar/ salvar
#Read = buscar/ selecionar
#Update = atualizar/ modificar
#Delete = apagar/ remover

#Criando a lista  de clientes 

lista_clientes = []

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