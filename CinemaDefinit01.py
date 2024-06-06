usuarios = {
    "clientes": [{"nome": "Neto", "senha": "senha_neto",
                  "idade": 15, "carteira_estudante": True, "cupom_cinema": False}],
    "admins": [{"nome": "Antonio", "senha": "senha_antonio"}]
}

filmes = [
    {
        "titulo": "Os Vingadores",
        "diretor": "Joss Whedon",
        "data_estreia": "04/05/2012",
        "horario_exibicao": "18:00",
        "valor_ingresso": 25.00,
        "sala": "Sala 1",
        "capacidade_sala": 100,
        "generos": ["Ação", "Aventura", "Ficção Científica"],
        "classificacao_indicativa": 12
    }
]

salas_disponiveis = ["Sala 1", "Sala 2", "Sala 3", "Sala 4", "Sala 5"]
cliente_logado = None
admin_logado = None

while True:
    print("\nBem-vindo ao Cinema!")
    print("1: Gerenciamento de filmes")
    print("2: Filmes em cartaz")
    print("3: Compra de ingresso")
    print("4: Cadastro de usuário")
    print("5: Entrar")
    print("6: Perfil")
    print("0: Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        if admin_logado:
            print("Opção 1 selecionada: Gerenciamento de filmes")
            while True:
                print("1: Realizar o cadastro do filme")
                print("2: Buscar filme")
                print("3: Atualizar dados do filme")
                print("4: Remover filme")
                print("0: Voltar ao MENU")

                sub_opcao = input("Escolha uma sub-opção: ")

                if sub_opcao == '1':
                    titulo = input("Digite o título do filme: ")
                    if any(filme["titulo"].lower() == titulo.lower() for filme in filmes):
                        print("Este filme já está cadastrado.")
                    else:
                        diretor = input("Digite o nome do diretor do filme: ")
                        data_estreia = input("Digite a data de estreia do filme (DD/MM/AAAA): ")
                        horario_exibicao = input("Digite o horário de exibição do filme (HH:MM): ")
                        valor_ingresso = float(input("Digite o valor do ingresso do filme: "))
                        generos = input("Digite os gêneros do filme (separados por vírgulas): ").split(',')
                        classificacao_indicativa = int(input("Digite a classificação indicativa do filme: "))

                        print("Salas disponíveis:")
                        for i, sala in enumerate(salas_disponiveis):
                            print(f"{i + 1}: {sala}")
                        sala_index = int(input("Escolha o número da sala de exibição: ")) - 1
                        sala = salas_disponiveis[sala_index]
                        capacidade_sala = int(input("Digite a capacidade da sala: "))

                        filmes.append({
                            "titulo": titulo,
                            "diretor": diretor,
                            "data_estreia": data_estreia,
                            "horario_exibicao": horario_exibicao,
                            "valor_ingresso": valor_ingresso,
                            "sala": sala,
                            "capacidade_sala": capacidade_sala,
                            "generos": [g.strip() for g in generos],
                            "classificacao_indicativa": classificacao_indicativa
                        })
                        salas_disponiveis.pop(sala_index)
                        print(f"Filme '{titulo}' cadastrado com sucesso!")

                elif sub_opcao == '2':
                    busca = input("Digite o nome do filme ou parte dele: ")
                    resultados = [filme for filme in filmes if busca.lower() in filme["titulo"].lower()]
                    if resultados:
                        print("Filmes encontrados:")
                        for i, filme in enumerate(resultados):
                            print(f"{i + 1}: {filme['titulo']}")
                        escolha_filme = int(input("Escolha o filme pelo número: ")) - 1
                        if 0 <= escolha_filme < len(resultados):
                            filme_escolhido = resultados[escolha_filme]
                            print("Detalhes do filme:")
                            print(f"Título: {filme_escolhido['titulo']}")
                            print(f"Diretor: {filme_escolhido['diretor']}")
                            print(f"Data de Estreia: {filme_escolhido['data_estreia']}")
                            print(f"Horário de Exibição: {filme_escolhido['horario_exibicao']}")
                            print(f"Valor do Ingresso: R${filme_escolhido['valor_ingresso']}")
                            print(f"Sala: {filme_escolhido['sala']}")
                            print(f"Capacidade da Sala: {filme_escolhido['capacidade_sala']}")
                            print(f"Gêneros: {', '.join(filme_escolhido['generos'])}")
                            print(f"Classificação Indicativa: {filme_escolhido['classificacao_indicativa']} anos")
                    else:
                        print("Nenhum filme encontrado com essa busca.")

                elif sub_opcao == '3':
                    busca = input("Digite o nome do filme ou parte dele: ")
                    resultados = [filme for filme in filmes if busca.lower() in filme["titulo"].lower()]
                    if resultados:
                        print("Filmes encontrados:")
                        for i, filme in enumerate(resultados):
                            print(f"{i + 1}: {filme['titulo']}")
                        escolha_filme = int(input("Escolha o filme pelo número: ")) - 1
                        if 0 <= escolha_filme < len(resultados):
                            filme_index = filmes.index(resultados[escolha_filme])
                            filme_escolhido = filmes[filme_index]

                            novo_titulo = input(f"Digite o novo título do filme (atual: {filme_escolhido['titulo']}): ")
                            novo_diretor = input(f"Digite o novo nome do diretor do filme (atual: {filme_escolhido['diretor']}): ")
                            nova_data_estreia = input(f"Digite a nova data de estreia do filme (atual: {filme_escolhido['data_estreia']}, formato DD/MM/AAAA): ")
                            novo_horario_exibicao = input(f"Digite o novo horário de exibição do filme (atual: {filme_escolhido['horario_exibicao']}, formato HH:MM): ")
                            novo_valor_ingresso = float(input(f"Digite o novo valor do ingresso do filme (atual: R${filme_escolhido['valor_ingresso']}): "))
                            novos_generos = input(f"Digite os novos gêneros do filme (atual: {', '.join(filme_escolhido['generos'])}, separados por vírgulas): ").split(',')
                            nova_classificacao_indicativa = int(input(f"Digite a nova classificação indicativa do filme (atual: {filme_escolhido['classificacao_indicativa']}): "))

                            print(f"Salas disponíveis (atual: {filme_escolhido['sala']}):")
                            for i, sala in enumerate(salas_disponiveis):
                                print(f"{i + 1}: {sala}")
                            sala_index = int(input("Escolha o número da nova sala de exibição (ou 0 para manter a mesma): ")) - 1
                            if sala_index == -1:
                                nova_sala = filme_escolhido['sala']
                            else:
                                nova_sala = salas_disponiveis[sala_index]
                                salas_disponiveis.pop(sala_index)

                            nova_capacidade_sala = int(input(f"Digite a nova capacidade da sala (atual: {filme_escolhido['capacidade_sala']}): "))

                            filme_escolhido.update({
                                "titulo": novo_titulo,
                                "diretor": novo_diretor,
                                "data_estreia": nova_data_estreia,
                                "horario_exibicao": novo_horario_exibicao,
                                "valor_ingresso": novo_valor_ingresso,
                                "sala": nova_sala,
                                "capacidade_sala": nova_capacidade_sala,
                                "generos": [g.strip() for g in novos_generos],
                                "classificacao_indicativa": nova_classificacao_indicativa
                            })
                            print(f"Filme '{novo_titulo}' atualizado com sucesso!")
                    else:
                        print("Nenhum filme encontrado com essa busca.")

                elif sub_opcao == '4':
                    busca = input("Digite o nome do filme ou parte dele: ")
                    resultados = [filme for filme in filmes if busca.lower() in filme["titulo"].lower()]
                    if resultados:
                        print("Filmes encontrados:")
                        for i, filme in enumerate(resultados):
                            print(f"{i + 1}: {filme['titulo']}")
                        escolha_filme = int(input("Escolha o filme pelo número: ")) - 1
                        if 0 <= escolha_filme < len(resultados):
                            filme_escolhido = resultados[escolha_filme]
                            filmes.remove(filme_escolhido)
                            salas_disponiveis.append(filme_escolhido['sala'])
                            print(f"Filme '{filme_escolhido['titulo']}' removido com sucesso!")
                    else:
                        print("Nenhum filme encontrado com essa busca.")

                elif sub_opcao == '0':
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Você precisa estar logado como administrador para acessar esta opção.")

    elif escolha == '2':
        print("Opção 2 selecionada: Filmes em cartaz")
        if filmes:
            for filme in filmes:
                print(f"Título: {filme['titulo']}, Diretor: {filme['diretor']}, Data de Estreia: {filme['data_estreia']}, Horário: {filme['horario_exibicao']}, Valor do Ingresso: R${filme['valor_ingresso']}, Sala: {filme['sala']}, Gêneros: {', '.join(filme['generos'])}, Classificação Indicativa: {filme['classificacao_indicativa']} anos")
        else:
            print("Nenhum filme em cartaz no momento.")

    elif escolha == '3':
        print("Opção 3 selecionada: Compra de ingresso")
        if cliente_logado:
            if filmes:
                for i, filme in enumerate(filmes):
                    print(f"{i + 1}: {filme['titulo']}")
                escolha_filme = int(input("Escolha o filme pelo número: ")) - 1
                if 0 <= escolha_filme < len(filmes):
                    filme = filmes[escolha_filme]
                    if cliente_logado["idade"] >= filme["classificacao_indicativa"]:
                        desconto = 1.0

                        # Desconto de 15% para menores de 14 anos e maiores de 60 anos
                        if cliente_logado["idade"] < 14 or cliente_logado["idade"] > 60:
                            desconto *= 0.85

                        # Desconto de 50% para estudantes
                        if cliente_logado["carteira_estudante"]:
                            desconto *= 0.5

                        valor_final = filme["valor_ingresso"] * desconto
                        print(f"Compra realizada com sucesso! Valor final: R${valor_final:.2f}")
                    else:
                        print(f"Você não tem idade suficiente para assistir a este filme. Classificação indicativa: {filme['classificacao_indicativa']} anos")
                else:
                    print("Filme selecionado inválido.")
            else:
                print("Nenhum filme em cartaz no momento.")
        else:
            print("Você precisa estar logado como cliente para comprar ingressos.")

    elif escolha == '4':
        print("Opção 4 selecionada: Cadastro de usuário")
        tipo_usuario = input("Você deseja se cadastrar como (1) Cliente ou (2) Administrador? ")
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")

        if tipo_usuario == '1':
            idade = int(input("Digite sua idade: "))
            carteira_estudante = input("Você possui carteira de estudante? (s/n): ").lower() == 's'
            usuarios['clientes'].append({"nome": nome, "senha": senha, "idade": idade, "carteira_estudante": carteira_estudante, "cupom_cinema": False})
            print("Cliente cadastrado com sucesso!")
        elif tipo_usuario == '2':
            usuarios['admins'].append({"nome": nome, "senha": senha})
            print("Administrador cadastrado com sucesso!")
        else:
            print("Opção inválida.")

    elif escolha == '5':
        print("Opção 5 selecionada: Entrar")
        if cliente_logado or admin_logado:
            print("Já existe um usuário logado. Por favor, deslogue primeiro.")
        else:
            tipo_usuario = input("Você deseja entrar como (1) Cliente ou (2) Administrador? ")
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            if tipo_usuario == '1':
                cliente = next((u for u in usuarios['clientes'] if u['nome'] == nome and u['senha'] == senha), None)
                if cliente:
                    cliente_logado = cliente
                    print(f"Bem-vindo, {cliente_logado['nome']}!")
                else:
                    print("Nome ou senha inválidos.")
            elif tipo_usuario == '2':
                admin = next((u for u in usuarios['admins'] if u['nome'] == nome and u['senha'] == senha), None)
                if admin:
                    admin_logado = admin
                    print(f"Bem-vindo, {admin_logado['nome']}!")
                else:
                    print("Nome ou senha inválidos.")
            else:
                print("Opção inválida.")

    elif escolha == '6':
        print("Opção 6 selecionada: Perfil")
        if cliente_logado or admin_logado:
            while True:
                if cliente_logado:
                    print(f"Cliente: {cliente_logado['nome']}")
                    print(f"Idade: {cliente_logado['idade']}")
                    print(f"Carteira de Estudante: {'Sim' if cliente_logado['carteira_estudante'] else 'Não'}")
                elif admin_logado:
                    print(f"Administrador: {admin_logado['nome']}")

                print("1: Deslogar")
                print("0: Menu Principal")
                perfil_opcao = input("Escolha uma opção: ")

                if perfil_opcao == '1':
                    cliente_logado = None
                    admin_logado = None
                    print("Usuário deslogado com sucesso!")
                    break
                elif perfil_opcao == '0':
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Você precisa estar logado para acessar o perfil.")

    elif escolha == '0':
        print("Obrigado por utilizar o sistema do Cinema!")
        break

    else:
        print("Opção inválida.")
