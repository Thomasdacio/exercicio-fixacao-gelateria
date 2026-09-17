import utils as u

print('Bem vindo a livraria do Thomas Dacio')

# Programa principal
# O código fica rodando até que o usuário digite '4' para encerrar
while True:
    print('-' * 46)
    print('-' * 15 + ' MENU PRINCIPAL ' + '-' * 15)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    
    opcao = input()
    
    if opcao == '1':
        u.cadastrar_livro(u.id_global)
        u.id_global += 1
    elif opcao == '2':
        u.consultar_livro()
    elif opcao == '3':
        u.remover_livro()
    elif opcao == '4':
        print('Encerrando programa...')
        break
    else:
        print('Opção inválida!')
        continue
                