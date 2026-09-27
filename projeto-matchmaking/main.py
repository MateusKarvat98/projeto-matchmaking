from models.Matchmaking import Matchmaking

servidor = Matchmaking()

while True:
    print("SELECIONE UMA OPÇÃO\n")
    print("1 - Cadastrar jogador")
    print("2 - Encontrar partida")
    print("3 - Sair da fila")
    print("4 - Encerrar sessão")
          
    escolha_menu = str(input("Selecione = "))

    match escolha_menu:
        case '1':
            nickname = input('\nPor favor insira seu nome de usuário: ')
            novo_jogador = servidor.cadastrar_jogador(nickname)
            print(f'Jogador {nickname} cadastrado com sucesso com o ID: {novo_jogador.id_jogador}')

        case '2':
            id_jogador_fila = input("Digite o ID que deseja adicionar a fila: ").strip()
            resultado = servidor.entrar_na_fila(id_jogador_fila)
            print(resultado)

        case '3':
            id_jogador_fila = input("Digite o ID que deseja remover da fila: ").strip()
            resultado = servidor.sair_fila(id_jogador_fila)
            print(resultado)        

        case '4':
            id_jogador_fila = input("Digite o ID que deseja encerrar sessão: ").strip()
            resultado = servidor.sair_fila(id_jogador_fila)
            print('Encerrando sistema...')
            break

        case _:
            print('Por favor, insira uma opção válida')
            

    