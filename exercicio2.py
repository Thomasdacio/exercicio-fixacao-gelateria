print('Bem-vindo a Loja de Gelados do Thomas Dacio')
print('--------------------Cardápio--------------------')
print('------------------------------------------------')
print('---|  Tamanho  |  Cupuaçu (CP)  | Açaí (AC) |---')
print('---|     P     |    R$  9.00    | R$ 11.00  |---')
print('---|     M     |    R$ 14.00    | R$ 16.00  |---')
print('---|     G     |    R$ 18.00    | R$ 20.00  |---')
print('------------------------------------------------')

total = 0

while True:

    sabor = input('Entre com o sabor desejado (CP/AC): ')

    if (sabor != 'cp' and sabor != 'ac'):
        print('Sabor inválido. Tente Novamente')
        continue

    elif (sabor == 'cp'):
                
        tam = input('Entre com o tamanho desejado (P/M/G): ')

        if (tam != 'p' and tam != 'm' and tam != 'g'):
            print('Tamanho inválido. Tente novamente')
            continue

        elif (tam == 'p'):
            print('Você pediu um Cupuaçu no tamanho P: R$9.00')
            total += 9
        

        elif (tam == 'm'):
            print('Você pediu um Cupuaçu no tamanho M: R$14.00')
            total += 14
            

        elif (tam == 'g'):
            print('Você pediu um Cupuaçu no tamanho G: R$18.00')
            total += 18

        comando = input('Deseja mais alguma coisa? (S/N): ')
        if (comando == 'n'):
            break
        elif (comando == 's'):
            continue
            

    elif (sabor == 'ac'):
                
        tam = input('Entre com o tamanho desejado (P/M/G): ')

        if (tam != 'p' and tam != 'm' and tam != 'g'):
            print('Tamanho inválido. Tente novamente')
            continue

        elif (tam == 'p'):
            print('Você pediu um Açaí no tamanho P: R$11.00')
            total += 11
        

        elif (tam == 'm'):
            print('Você pediu um Açaí no tamanho M: R$16.00')
            total += 16
            

        elif (tam == 'g'):
            print('Você pediu um Açaí no tamanho G: R$20.00')
            total += 20

        comando = input('Deseja mais alguma coisa? (S/N): ')
        if (comando == 'n'):
            break
        elif (comando == 's'):
            continue

print(f'O valor total a ser pago: R$ {total:.2f}')