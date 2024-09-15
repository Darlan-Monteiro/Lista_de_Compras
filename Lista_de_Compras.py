lista_compras = []

def adicionar():
    while True:
        produto = input('\nDigite o produto que deseja adicionar (ou deixe vazio para cancelar): ').strip().upper()
        
        if produto == "":
            print("\nNenhum produto adicionado.")
            break
        elif produto in lista_compras:
            print('\nO produto já está em sua lista de compras.\nInsira um novo produto ou deixe vazio para cancelar.')
        else:
            lista_compras.append(produto)
            print(f'\n{produto} foi adicionado à lista de compras.')
            break
    
def remover_item():
    produto_remover = input('\nDigite o nome do produto que deseja remover: ').strip().upper()
    
    if produto_remover in lista_compras:
        lista_compras.remove(produto_remover)
        print(f'\n{produto_remover} removido com sucesso.')
    else:
        print('\nProduto não encontrado! Tente novamente.')
        
def limpar_lista():
    while True:
        confirmacao = input('\nDeseja remover todos os itens da lista? SIM/NÃO: ').strip().upper()
        if confirmacao == "SIM":
            lista_compras.clear()
            print('\nTodos os itens foram removidos da sua lista de compras.')
            break
        elif confirmacao == "NÃO":
            print('\nNenhum item foi removido.')
            break
        else:
            print('\nResposta inválida. Por favor, digite SIM ou NÃO.')

def ver_lista():
    if lista_compras:
        print('\nSua lista de compras:')
        for item in lista_compras:
            print(f'- {item}')
    else:
        print('\nSua lista de compras está vazia.')

# Início do programa
print('-----------------------------------')
print('| Bem-Vindo(a) a CODE DREAMS LIST |')
print('-----------------------------------\n')
nome = input('Digite o seu nome: ').title().strip()

print(f'\n- Olá, {nome}! É bom te ver por aqui. 😉')
print('  ---------------------------------------------')

while True:
    print('\n\n-----------------------------------')
    print('|               MENU              |')
    print('-----------------------------------\n')

    print(' 1 - Adicionar item à lista \n 2 - Remover um item da lista\n 3 - Limpar todos os itens da lista\n 4 - Ver lista\n 5 - Sair\n')

    try:
        opcao = int(input('Só serão aceitos os números inteiros: 1, 2, 3, 4 ou 5.\nDigite a opção desejada: ').strip())

        # Verifica se a opção está dentro do intervalo esperado
        if opcao not in range(1, 6):
            print("\nOpção inválida! Por favor, insira um número entre 1 e 5.")
            continue

        # Usando o match-case para processar a opção
        match opcao:
            case 1:
                adicionar()
            case 2:
                remover_item()
            case 3:
                limpar_lista()
            case 4:
                ver_lista()
            case 5:
                print('Saindo...')
                break
    
    except ValueError:
        print("\nValor inválido! Por favor, insira um número inteiro.")
