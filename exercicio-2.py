print('Bem vindo a copiadora do Thomas Dacio')

def escolha_servico():

    while True:

        print('Entre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')

        servico = input('')

        if ((servico != 'dig') and (servico != 'ico') and (servico != 'ipb') and (servico != 'fot')):
                print('Escolha inválida, entre com o tipo de serviço novamente...')
                continue

        elif (servico == 'dig'):
             servico = 1.10
             return servico
        
        elif (servico == 'ico'):
            servico = 1
            return servico
        
        elif (servico == 'ipb'):
            servico = 0.40
            return servico
        
        elif (servico == 'fot'):
             servico = 0.20
             return servico

servico = escolha_servico()

def num_pagina(servico):

    while True:
     
        try:
            n_pag = int(input('Entre com o número de páginas: '))

            if (n_pag >= 20000):
                 print('Não aceitamos tantas páginas de uma vez. \n Por favor, entre com o número de páginas novamente.')
                 continue

            elif (n_pag < 20):
                 return n_pag * servico
            
            if (20 <= n_pag < 200):
                 return (n_pag * servico) - ((n_pag * servico) * 0.15)
            
            if (200 <= n_pag < 2000):
                 return (n_pag * servico) - ((n_pag * servico) * 0.20)
            
            if (2000 <= n_pag < 20000):
                 return (n_pag * servico) - ((n_pag * servico) * 0.25)
                    
        except ValueError:

            print('Você deve digitar um número...')

n_pag = num_pagina(servico)  

def servico_extra():

    while True:

        print('Deseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$ 15.00')
        print('2 - Encadernação Capa Dura - R$ 40.00')
        print('0 - Não desejo mais nada')
        extra = input('')

        if ((extra != '1') and (extra != '2') and (extra != '0')):
             print('Entre com uma opção válida...')
             continue

        elif (extra == '1'):
             return 15
        
        elif (extra == '2'):
             return 40
        
        elif (extra == '0'):
             return 0

extra = servico_extra()

total = (servico * n_pag) + extra
print(f'Total: R$ {total:.2f} (serviço: {servico} * páginas: {n_pag} + extra: {extra:.2f})')

