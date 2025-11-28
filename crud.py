import os
import time
from dataclasses import dataclass

os.system("cls || clear")

lista_clientes = []


# CRUD usando dataclass para representar clientes
@dataclass
class Cliente:
    nome: str
    idade: int
    email: str
    telefone: str

    # Método para mostrar os dados do cliente
    def mostrar_dados(self):
        print(f"Nome: {self.nome}, idade: {self.idade}, email: {self.email}, telefone: {self.telefone}")


# Função para verificar se a lista está vazia
def lista_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNão há clientes cadastrados.")
        return True
    return False


# Função para adicionar um cliente na lista
def adicionar_cliente(lista_clientes):
    print("\nAdicionar cliente:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("Email: ")
    telefone = input("Telefone: ")

    novo_cliente = Cliente(nome, idade, email, telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")


# Função para encontrar um cliente na lista de clientes
def encontrar_cliente_por_email(lista_clientes, email_busca):
    email_busca = email_busca.lower()
    for cliente in lista_clientes:
        if cliente.email.lower() == email_busca:
            return cliente
    # o return None tem que ficar FORA do for
    return None


# Função para mostrar todos os clientes
def mostrar_todos_clientes(lista_clientes):
    if lista_vazia(lista_clientes):
        return
    print("\nLista de clientes:")
    for cliente in lista_clientes:
        # mostrar_dados já faz o print, não precisa formatar dentro de f-string
        cliente.mostrar_dados()


# Função para atualizar os dados de um cliente
def atualizar_cliente(lista_clientes):
    if lista_vazia(lista_clientes):
        return

    mostrar_todos_clientes(lista_clientes)
    print("\nAtualizar cliente:")
    email_busca = input("\nDigite o email do cliente que deseja atualizar: ")
    cliente_atualizar = encontrar_cliente_por_email(lista_clientes, email_busca)

    if cliente_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"Nome atual: {cliente_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"Idade atual: {cliente_atualizar.idade}")
        nova_idade = input("Nova idade: ")

        print(f"Email atual: {cliente_atualizar.email}")
        novo_email = input("Novo email: ")

        print(f"Telefone atual: {cliente_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome:
            cliente_atualizar.nome = novo_nome
        if nova_idade:
            cliente_atualizar.idade = int(nova_idade)
        if novo_email:
            cliente_atualizar.email = novo_email
        if novo_telefone:
            cliente_atualizar.telefone = novo_telefone

        print(f"\nDados do cliente {cliente_atualizar.email} atualizados com sucesso!")
    else:
        print(f"\nCliente {email_busca} não encontrado na lista.")


# Função para remover um cliente da lista
def remover_cliente(lista_clientes):
    if lista_vazia(lista_clientes):
        return

    mostrar_todos_clientes(lista_clientes)

    email_remover = input("\nDigite o nome do cliente que deseja remover: ")
    cliente_encontrado = encontrar_cliente_por_email(lista_clientes, email_remover)

    if cliente_encontrado:
        # aqui o erro era remover(remover_cliente) em vez de remover(cliente_encontrado)
        lista_clientes.remove(cliente_encontrado)
        print(f"\nCliente {email_remover} removido com sucesso!")
    else:
        print(f"\nCliente {email_remover} não encontrado na lista.")


# Menu de opções
while True:
    print('''

--- Menu de opções ----
1 - Adicionar cliente
2 - Mostrar todos os clientes
3 - Atualizar cliente
4 - Remover cliente
5 - Sair
''')
    opcao = input("Escolha uma opção (1-5): ")

    match opcao:
        case '1':
            adicionar_cliente(lista_clientes)
        case '2':
            mostrar_todos_clientes(lista_clientes)
        case '3':
            atualizar_cliente(lista_clientes)
        case '4':
            remover_cliente(lista_clientes)
        case '5':
            print("\nSaindo do programa...")
            time.sleep(2)
            os.system("cls || clear")
            break
        case _:
            print("\nOpção inválida, tente novamente.")
