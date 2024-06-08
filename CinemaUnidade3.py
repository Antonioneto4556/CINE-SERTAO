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
        "classificacao_indicativa": 12,
        "ingressos_vendidos": 0  # Novo campo para rastrear vendas
    }
]

salas_disponiveis = ["Sala 2", "Sala 3", "Sala 4", "Sala 5"]
cliente_logado = None
admin_logado = None


def ordenar_por_ingressos(filme):
    return filme['ingressos_vendidos']


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
            while True:
                print("\nGerenciamento de Filmes:")
                print("1: Cadastrar novo filme")
                print("2: Buscar filme")
                print("3: Atualizar dados do filme")
                print("4: Remover filme")
                print("5: Listar todos os filmes")
                print("6: Gerenciar salas de exibição")
                print("7: Gerenciar gêneros de filmes")
                print("8: Visualizar vendas de ingressos")
                print("9: Definir promoções e descontos")
                print("0: Sair do gerenciamento de filmes")

                sub_opcao = input("Escolha uma opção: ")

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
                            "classificacao_indicativa": classificacao_indicativa,
                            "ingressos_vendidos": 0
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
                            print(f"Ingressos Vendidos: {filme_escolhido['ingressos_vendidos']}")
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
                            novo_diretor = input(
                                f"Novo nome do diretor do filme (atual: {filme_escolhido['diretor']}): ")
                            nova_data_estreia = input(
                                f"Nova data de estreia (atual:{filme_escolhido['data_estreia']}, formato DD/MM/AAAA): ")
                            novo_horario_exibicao = input(
                                f"Novo horário de exibição (atual: {filme_escolhido['horario_exibicao']}, formato HH:MM): ")
                            novo_valor_ingresso = float(input(
                                f"Novo valor do ingresso (atual: R${filme_escolhido['valor_ingresso']}): "))
                            novos_generos = input(
                                f"Novos gêneros do filme (atual: {', '.join(filme_escolhido['generos'])}, separados por vírgulas): ").split(',')
                            nova_classificacao_indicativa = int(input(
                                f"Nova classificação indicativa (atual: {filme_escolhido['classificacao_indicativa']}): "))

                            print(f"Salas disponíveis (atual: {filme_escolhido['sala']}):")
                            for i, sala in enumerate(salas_disponiveis):
                                print(f"{i + 1}: {sala}")
                            sala_index = int(
                                input("Escolha o número da nova sala de exibição (ou 0 para manter a mesma): ")) - 1
                            if sala_index == -1:
                                nova_sala = filme_escolhido['sala']
                            else:
                                nova_sala = salas_disponiveis[sala_index]
                                salas_disponiveis.pop(sala_index)

                            nova_capacidade_sala = int(input(
                                f"Digite a nova capacidade da sala (atual: {filme_escolhido['capacidade_sala']}): "))

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
                            salas_disponiveis.append(filme_escolhido["sala"])
                            filmes.remove(filme_escolhido)
                            print(f"Filme '{filme_escolhido['titulo']}' removido com sucesso!")
                    else:
                        print("Nenhum filme encontrado com essa busca.")

                elif sub_opcao == '5':
                    print("Lista de todos os filmes:")
                    for filme in filmes:
                        print(
                            f" Título: {filme['titulo']},"
                            f" Diretor: {filme['diretor']},"
                            f" Sala: {filme['sala']},"
                            f" Capacidade: {filme['capacidade_sala']},"
                            f" Gêneros: {', '.join(filme['generos'])},"
                            f" Classificação: {filme['classificacao_indicativa']}")

                elif sub_opcao == '6':
                    print("Salas de Exibição Disponíveis:")
                    for i, sala in enumerate(salas_disponiveis):
                        print(f"{i + 1}: {sala}")
                    sala_nova = input("Digite o nome da nova sala de exibição ou pressione Enter para sair: ")
                    if sala_nova:
                        if sala_nova not in salas_disponiveis:
                            salas_disponiveis.append(sala_nova)
                            print(f"Sala '{sala_nova}' adicionada com sucesso!")
                        else:
                            print("Essa sala já existe.")

                elif sub_opcao == '7':
                    print("Gerenciamento de Gêneros de Filmes:")
                    generos_existentes = set([g for filme in filmes for g in filme['generos']])
                    for i, genero in enumerate(generos_existentes):
                        print(f"{i + 1}: {genero}")
                    genero_novo = input("Digite o novo gênero ou pressione Enter para sair: ")
                    if genero_novo:
                        if genero_novo not in generos_existentes:
                            generos_existentes.add(genero_novo)
                            print(f"Gênero '{genero_novo}' adicionado com sucesso!")
                        else:
                            print("Esse gênero já existe.")

                elif sub_opcao == '8':
                    print("Vendas de Ingressos:")
                    for filme in filmes:
                        print(f"Filme: {filme['titulo']}, Ingressos Vendidos: {filme['ingressos_vendidos']}")

                elif sub_opcao == '9':
                    print("Definir Promoções e Descontos:")
                    titulo = input("Digite o título do filme para aplicar a promoção: ")
                    filme_promocao = next((filme for filme in filmes if filme['titulo'].lower() == titulo.lower()),
                                          None)
                    if filme_promocao:
                        desconto = float(input("Digite o percentual de desconto (por exemplo, 10 para 10%): "))
                        valor_desconto = filme_promocao['valor_ingresso'] * (desconto / 100)
                        filme_promocao['valor_ingresso'] -= valor_desconto
                        print(
                            f"Desconto de {desconto}% aplicado ao filme '{filme_promocao['titulo']}'. Novo valor do ingresso: R${filme_promocao['valor_ingresso']}")
                    else:
                        print("Filme não encontrado.")

                elif sub_opcao == '0':
                    break

                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print("Acesso negado. Faça login como administrador para acessar o gerenciamento de filmes.")

    elif escolha == '2':
        filmes_ordenados = sorted(filmes, key=ordenar_por_ingressos, reverse=True)[:5]
        print("Filmes em Cartaz (Top 5):")
        for filme in filmes_ordenados:
            print(
                f"Título: {filme['titulo']}, Diretor: {filme['diretor']}, Data de Estreia: {filme['data_estreia']}, Horário de Exibição: {filme['horario_exibicao']}, Sala: {filme['sala']}, Gêneros: {', '.join(filme['generos'])}, Classificação Indicativa: {filme['classificacao_indicativa']}, Ingressos Vendidos: {filme['ingressos_vendidos']}")

    elif escolha == '3':
        print("Compra de ingresso")
        nome_cliente = input("Digite seu nome: ")
        idade_cliente = int(input("Digite sua idade: "))
        filme_escolhido = input("Digite o título do filme que deseja assistir: ")
        filme_encontrado = next((filme for filme in filmes if filme["titulo"].lower() == filme_escolhido.lower()), None)
        if filme_encontrado:
            if idade_cliente >= filme_encontrado["classificacao_indicativa"]:
                if filme_encontrado["ingressos_vendidos"] < filme_encontrado["capacidade_sala"]:
                    filme_encontrado["ingressos_vendidos"] += 1
                    print(f"Ingresso comprado com sucesso para o filme '{filme_encontrado['titulo']}'!")
                else:
                    print("Desculpe, todos os ingressos para este filme foram vendidos.")
            else:
                print("Desculpe, você não tem idade suficiente para assistir a este filme.")
        else:
            print("Filme não encontrado.")

    elif escolha == '4':
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        tipo_usuario = input("Digite o tipo de usuário (cliente/admin): ")

        if tipo_usuario.lower() == "cliente":
            idade = int(input("Digite sua idade: "))
            carteira_estudante = input("Possui carteira de estudante? (s/n): ").lower() == 's'
            cupom_cinema = input("Possui cupom de desconto? (s/n): ").lower() == 's'
            usuarios["clientes"].append(
                {"nome": nome, "senha": senha, "idade": idade, "carteira_estudante": carteira_estudante,
                 "cupom_cinema": cupom_cinema})
            print(f"Cliente {nome} cadastrado com sucesso!")

        elif tipo_usuario.lower() == "admin":
            usuarios["admins"].append({"nome": nome, "senha": senha})
            print(f"Admin {nome} cadastrado com sucesso!")

        else:
            print("Tipo de usuário inválido.")

    elif escolha == '5':
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")

        cliente = next((c for c in usuarios["clientes"] if c["nome"] == nome and c["senha"] == senha), None)
        admin = next((a for a in usuarios["admins"] if a["nome"] == nome and a["senha"] == senha), None)

        if cliente:
            cliente_logado = cliente
            print(f"Bem-vindo, {cliente['nome']}!")
        elif admin:
            admin_logado = admin
            print(f"Bem-vindo, {admin['nome']}! (Admin)")
        else:
            print("Nome ou senha incorretos.")

    elif escolha == '6':
        if cliente_logado:
            print(f"Perfil do cliente: {cliente_logado['nome']}")
            print(f"Idade: {cliente_logado['idade']}")
            print(f"Carteira de Estudante: {'Sim' if cliente_logado['carteira_estudante'] else 'Não'}")
            print(f"Cupom de Desconto: {'Sim' if cliente_logado['cupom_cinema'] else 'Não'}")
        else:
            print("Nenhum cliente logado.")

    elif escolha == '0':
        break

    else:
        print("Opção inválida. Tente novamente.")
