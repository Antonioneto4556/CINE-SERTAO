from time import sleep

usuarios = {'Antonio': {'senha': 'neto123', 'perfil': 'admin'},
            'Neto': {'senha': '123', 'perfil': 'cliente'}
            }
salas = set()
filmes = {"Jalin Habei": {"sala": 1, "horario": "18:00", "capacidade": 75, "valor": 20.00, "ingressos_vendidos": 0},
          "Tomas Turbano": {"sala": 2, "horario": "19:30", "capacidade": 80, "valor": 18.00, "ingressos_vendidos": 0},
          "Two Girls and a Cup": {"sala": 3, "horario": "20:15", "capacidade": 90, "valor": 15.00, "ingressos_vendidos": 0},
          "Naruto: O Gari de Konoha": {"sala": 4, "horario": "20:15", "capacidade": 90, "valor": 15.00, "ingressos_vendidos": 0}
          }
for filme in filmes.values():
    salas.add(filme["sala"])
while True:
    print('\n\033[95:40m}======[ \033[m\033[1:3:97:40mCINE SERTÃO\033[m\033[95:40m ]======{\033[0m')
    print('\033[7:91:40m[ 1 ]\033[m\033[7:94:40m | GERENCIAR OS FILMES |\033[m')
    print('\033[7:91:40m[ 2 ]\033[m\033[94:40m | COMPRAR  INGRESSOS  |\033[m')
    print('\033[7:91:40m[ 3 ]\033[m\033[7:94:40m | FILMES  EM  CARTAZ  |\033[m')
    print('\033[7:91:40m[ 4 ]\033[m\033[94:40m | CADASTRAR  USUARIO  |\033[m')
    print('\033[7:90:40m[ 0 ]\033[m\033[7:91:40m | SAIR   DO   MENU    |\033[m')

    opcaoM = int(input(f'\033[1:3:7:40m Escolha uma opção:          \033[m'))
    print()
    if(opcaoM == 1):
        sleep(1)
        while True:
            print('[APENAS PARA ADMINISTRADORES]')
            usuario = input('Digite o nome de usuário: ')
            senha = input('Digite a senha: ')
            if(usuario in usuarios and usuarios[usuario]['senha'] == senha):
                print('Login bem-sucedido!')
                break
            else:
                print('\033[91mUsuário ou senha incorretos. Tente novamente.\033[m')

        if(usuarios[usuario]['perfil'] == 'admin'):
            while True:
                print('\n\033[94m=== Módulo de Gerenciamento de Filmes ===\033[0m')
                print('\033[0:92:41m[1]\033[m Cadastrar Filme')
                print('\033[0:92:41m[2]\033[m Buscar Filme')
                print('\033[0:92:41m[3]\033[m Atualizar Filme')
                print('\033[0:92:41m[4]\033[m Remover Filme')
                print('\033[0:92:41m[5]\033[m Visualizar vendas de ingressos')
                print('\033[0:92:41m[0]\033[m Voltar ao menu principal')

                opcao = int(input('Escolha uma opção: '))
                if(opcao == 1):
                    sleep(1)
                    print('\nCadastro de Filme')
                    titulo = input('Título do Filme: ')
                    sala = int(input('Sala: '))
                    while sala in salas:
                        print('Sala já cadastrada. Escolha outra sala.')
                        sala = int(input('Sala: '))
                    salas.add(sala)
                    horario = input('Horário: ')
                    capacidade = int(input('Capacidade: '))
                    valor = float(input('Valor do Ingresso: '))
                    filmes[titulo] = {'sala': sala,'horario': horario,'capacidade': capacidade,
                                      'valor': valor,'ingressos_vendidos': 0}
                    print('\033[92mFilme cadastrado com sucesso!\033[m')
                elif(opcao == 2):
                    sleep(1)
                    print('\n\033[94mBusca de Filme\033[m')
                    titulo = input('Digite o título do filme: ')
                    if(titulo in filmes):
                        print('\033[92mFilme encontrado:\033[m')
                        print(filmes[titulo])
                    else:
                        Moves_semelhantes = []
                        for filme_titulo in filmes.keys():
                            if(titulo.lower() in filme_titulo.lower()):
                                Moves_semelhantes.append(filme_titulo)
                        if(Moves_semelhantes):
                            print('\033[91mFilme não encontrado\033[m. \033[94mFilmes semelhantes:\033[m')
                            for filme in Moves_semelhantes:
                                print(filme)
                                sleep(1)        
                        else:
                            print('\033[91mFilme não encontrado.\033[m')
                elif(opcao == 3):
                    sleep(1)
                    print('\nAtualizar Filme')
                    titulo = input('Digite o título do filme que deseja atualizar: ')
                    if(titulo in filmes):
                        print('Filme encontrado. Atualize as informações: ')
                        filmes[titulo]["sala"] = input('Nova Sala: ')
                        filmes[titulo]["horario"] = input('Novo Horário: ')
                        filmes[titulo]["capacidade"] = int(input('Nova Capacidade: '))
                        filmes[titulo]["valor"] = float(input('Novo Valor do Ingresso: '))
                        print('Filme atualizado com sucesso!')
                    else:
                        Moves_semelhantes = []
                        for filme_titulo in filmes.keys():
                            if(titulo.lower() in filme_titulo.lower() or filme_titulo.lower() in titulo.lower()):
                                Moves_semelhantes.append(filme_titulo)
                        if(Moves_semelhantes):
                            print('Filme não encontrado. Filmes semelhantes:')
                            for filme in Moves_semelhantes:
                                print(filme)
                        else:
                            print('Filme não encontrado.')
                elif(opcao == 4):
                    sleep(1)
                    print("\nRemover Filme")
                    titulo = input('Digite o título do filme que deseja remover: ')
                    if(titulo in filmes):
                        del filmes[titulo]
                        print("Filme removido com sucesso!")
                    else:
                        Moves_semelhantes = []
                        for filme_titulo in filmes.keys():
                            if(titulo.lower() in filme_titulo.lower() or filme_titulo.lower() in titulo.lower()):
                                Moves_semelhantes.append(filme_titulo)
                        if(Moves_semelhantes):
                            print('Filme não encontrado. Filmes semelhantes:')
                            for filme in Moves_semelhantes:
                                print(filme)
                        else:
                            print('Filme não encontrado.')
                elif(opcao == 5):
                    sleep(1)
                    print('\nVendas de Ingressos')
                    for titulo, filme in filmes.items():
                        print(f'Filme: {titulo}, Ingressos Vendidos: {filme['ingressos_vendidos']},Valor Total Arrecadado: R$ {filme['ingressos_vendidos'] * filme['valor']:.2f}')
                elif(opcao == 0):
                    sleep(1)
                    break
                else:
                    print('Opção inválida!')
        else:
            print('Acesso negado! Esta função é exclusiva para administradores.')

    elif(opcaoM == 2):
        sleep(1)
        while True:
            usuario = input('Digite o nome de usuário: ')
            senha = input('Digite a senha: ')
            if(usuario in usuarios and usuarios[usuario]['senha'] == senha):
                print('Login bem-sucedido!')
                break
            else:
                print('Usuário ou senha incorretos. Tente novamente.')

        if(usuarios[usuario]['perfil'] == 'cliente'):
            print('\nCompra de Ingresso')
            print('Filmes Disponíveis:')
            for titulo, filme in filmes.items():
                print(f'{titulo} - R$ {filme['valor']:.2f}')
            titulo = input("Digite o título do filme que deseja assistir: ")
            if(titulo in filmes):
                filme = filmes[titulo]
                if(filme['capacidade'] > 0):
                    filme['capacidade'] -= 1
                    filme['ingressos_vendidos'] += 1
                    print(f'Ingresso comprado com sucesso para {titulo}. Aproveite o filme!')
                else:
                    print('Desculpe, a capacidade máxima para este filme foi atingida.')
            else:
                Moves_semelhantes = []
                for filme_titulo in filmes.keys():
                    if(titulo.lower() in filme_titulo.lower() or filme_titulo.lower() in titulo.lower()):
                        Moves_semelhantes.append(filme_titulo)
                if(Moves_semelhantes):
                    print('Filme não encontrado. Filmes semelhantes:')
                    for filme in Moves_semelhantes:
                        print(filme)
                else:
                    print('Filme não encontrado.')
        else:
            print('Apenas clientes podem comprar ingressos!')

    elif(opcaoM == 3):
        sleep(1)
        while True:
            print('\033[97m-=\033[m'*34)
            print('FILMES DISPONÍVEIS:')
            print('\033[97m-=\033[m' * 34)
            for titulo, filme in filmes.items():
                print(f'\033[94m{titulo}\033[m - \033[94m{filme['sala']}\033[m - \033[91m{filme['horario']}\033[m - \033[92mR$ {filme['valor']:.2f}\033[m - \033[96m{filme['capacidade']} lugares disponíveis\033[m')
            voltandoM = str(input('Digite \033[92m[V]\033[m para volta ao \033[92mMENU\033[m:')).upper()
            if(voltandoM == 'V'):
                sleep(1)
                break
            else:
                sleep(1)
    elif(opcaoM == 4):
        (sleep(1))
        while True:
            print(' ===== CADASTRO ===== ')
            novo_usuario = input('Nome de Usuário: ')
            if(novo_usuario not in usuarios):
                senha = input('Senha: ')
                perfil = input('Perfil [admin] ou [cliente]: ')
                usuarios[novo_usuario] = {'senha': senha, 'perfil': perfil}
                print('Usuário cadastrado com sucesso!')
                novo_cadastro = int(input('Para cadastra novamente digite [1]\ncaso queira voltar ao menu digite [2]'))
                if(novo_cadastro == 2):
                    sleep(1)
                    break
                else:
                    print()
            else:
                print('\033[91mNOME DE USUARIO JÁ CADASTRADO\033[m. \033[94mEscolha outro.\033[m')

    elif(opcaoM == 0):
        sleep(1)
        desejo = input('Deseja sair do CINE Sertão? (S|N): ').upper()
        if(desejo == 'S'):
            print('\033[97mFechando o CINE Sertão\033[m', end='')
            (sleep(1))
            print('\033[93m.\033[m', end='')
            (sleep(1))
            print('\033[91m.\033[m', end='')
            (sleep(1))
            print('\033[92m.\033[m', end='')
            (sleep(1))
            print('\033[7:91:40mENCERRADO\033[m')
            break
        elif(desejo == 'N'):
            print('Voltando ao MENU!')
            sleep(1)
        else:
            print('\033[91mOPÇÃO INVÁLIDA!\033[m')
            sleep(1)
    else:
        sleep(1)
        print('\033[91mOPÇÃO INVÁLIDA!\033[m')
