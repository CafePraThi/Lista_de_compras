

lista = []

while True:
    print('Selecione uma opção abaixo:')
    opcao = input("[I]nserir  [A]pagar  [L]istar: ").lower()

    if opcao == 'i':
        item = input("Escreva o item a ser adicionado: ")
        lista.append(item)

    elif opcao == 'a':
        apagar = input('Escolha o item para apagar: ')

        try:
            indice = int(apagar)
            del lista[indice]
        except ValueError:
            print("Digite um numero valido!")
        except Exception:
            print("Esse Indice não existe!")
        except:
            print("Error!")

    elif opcao == 'l':
        if len(lista) == 0:
            print("Sua lista esta vazia!")

        for i, item in enumerate(lista):
            print(i, item)
    else:
        print("Por favor escolha uma das opçoes validas")
