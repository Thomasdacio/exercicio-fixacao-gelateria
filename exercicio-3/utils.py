lista_livros = list()
id_global = 6046640

# FUNÇÃO CADASTRAR LIVRO
# Ao usuário digitar os dados do livro, eles são depositados em um dicionário e depois ele é adicionado à lista de livros

def cadastrar_livro(id):
    print('-' * 52)
    print('-' * 15 + ' MENU CADASTRAR LIVRO ' + '-' * 15)
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o nome do autor do livro: ')
    editora = input('Digite o nome da editora do livro: ')
    print('-' * 46)
    print()
    id += 1
    novo_dicionario = {'ID': id, 'Nome': nome, 'Autor':autor, 'Editora': editora}
    novo_dicionario['ID'] = id
    novo_dicionario['Nome'] = nome
    novo_dicionario['Autor'] = autor
    novo_dicionario['Editora'] = editora
    lista_livros.append(novo_dicionario.copy())
    
# FUNÇÃO CONSULTAR LIVRO
# Aqui o usuário escolhe como quer consultar o(s) livro(s)

def consultar_livro():
    
    while True:
        print('-' * 52)
        print('-' * 15 + ' MENU CONSULTAR LIVRO ' + '-' * 15)
        print('Escolha a opção desejada: ')
        print('1 - Consultar Todos os Livros')
        print('2 - Consultar Livro por ID')
        print('3 - Consultar Livro(s) por autor')
        print('4 - Retornar')
        
        opcao = input()
        livro_encontrado = False
        
        if opcao == '1':
            for livro in lista_livros:
                if livro:
                    livro_encontrado = True
                    print(f'ID: {livro['ID']}')
                    print(f'Nome: {livro['Nome']}')
                    print(f'Autor: {livro['Autor']}')
                    print(f'Editora: {livro['Editora']}')
                    print()
            if livro_encontrado != True:
                print('Nenhum livro encontrado!')
                
        elif opcao == '2':
            id_livro = int(input('Digite o ID do livro: '))
            for livro in lista_livros:
                if livro['ID'] == id_livro:
                    livro_encontrado = True
                    print(f'Nome: {livro['Nome']}')
                    print(f'Autor: {livro['Autor']}')
                    print(f'Editora: {livro['Editora']}')
                    print()
                        
            if livro_encontrado != True:
                print('Nenhum livro encontrado!')
                    
        elif opcao == '3':
            autor_livro = input('Digite o Autor do livro: ')
            for livro in lista_livros:
                if livro['Autor'] == autor_livro:
                    livro_encontrado = True
                    print(f'ID: {livro['ID']}')
                    print(f'Nome: {livro['Nome']}')
                    print(f'Autor: {livro['Autor']}')
                    print(f'Editora: {livro['Editora']}')
                    print()
                        
            if livro_encontrado != True:
                print('Nenhum livro encontrado!')
                    
        elif opcao == '4':
            break
                    
        else:
            print('Digite uma opção válida!')
            continue
        
def remover_livro():
    
    print('-' * 50)
    print('-' * 15 + ' MENU REMOVER LIVRO ' + '-' * 15)
    id_livro = int(input('Digite o ID do livro: '))
    livro_encontrado = False
    
    for livro in lista_livros:
        if livro['ID'] == id_livro:
            livro_encontrado = True
            lista_livros.remove(livro)
    if livro_encontrado == True:
        print('Livro removido com sucesso!')
    else:
        print('Nenhum livro encontrado!')
            