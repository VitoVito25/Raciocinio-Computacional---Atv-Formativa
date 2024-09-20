from utils import clear_console
import json
import os

# Dicionário para mapear opções a descrições do menu principal
gerOpcoes = {
    1: "Estudantes",
    2: "Professores",
    3: "Disciplinas",
    4: "Turmas",
    5: "Matriculas",
    9: "Sair"
}

# Dicionário para mapear opções a descrições do menu secundário
secOpcoes = {
    1: "Incluir",
    2: "Listar",
    3: "Atualizar",
    4: "Excluir",
    9: "Voltar ao menu principal"
}

# Dicionário para mapear opções de configuração e nome dos arquivos
gerConfig = {
    1: "estudantes",
    2: "professores",
    3: "disciplinas",
    4: "turmas",
    5: "matriculas"
}

# Estrutura de listagem de dados
estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []

# Mapeia os arrays de dados para os tipos correspondentes
arrays_dados = {
    1: estudantes,
    2: professores,
    3: disciplinas,
    4: turmas,
    5: matriculas
}

def inicio():
    """
        Função para chamar inicio do programa e visualizar se temos dados recuperados

        :param: Não é necessario a inclusão de parametros
        :return: Não retorna valores
    """

    print("----- SISTEMA DE GERENCIAMENTO DE FACULDADE -----")
    recuperarTodosDadosEmMemoria()
    input("Pressione ENTER para continuar...")
    clear_console()

def menuPrincipal():
    """
        Função para chamar o menu principal

        :param: Não é necessario a inclusão de parametros
        :return gerTipo: Retorna o int para a identificação de qual o menu selecionado
        :return gerDesc: Retorna o descritivo para a identificação de qual o menu selecionado
    """

    while True:
        # Estrutura menu principal
        print("------ MENU PRINCIPAL ------\n")
        print("(1) Gerenciar Estudantes")
        print("(2) Gerenciar Professores")
        print("(3) Gerenciar Disciplinas")
        print("(4) Gerenciar Turmas")
        print("(5) Gerenciar Matriculas")
        print("(9) Sair")
        try:
            # Solicita que o usuário insira uma opção
            gerTipo = int(input("Informe a opção desejada: "))

            # Obtém o valor correspondente ou define como "opção inválida"
            gerDesc = gerOpcoes.get(gerTipo, "Opção inválida")

            # Verifica se a opção é válida
            if gerTipo not in gerOpcoes:
                clear_console()
                print("----- [{}] VOLTANDO AO MENU PRINCIPAL... -----\n".format(gerDesc).upper())
                continue

            # Verifica se o usuário escolheu sair
            if gerTipo == 9:
                clear_console()
                print("----- SAINDO DO SISTEMA... -----")
                break
            
            # Se o gerTipo é válido e não é 9, sai do loop
            break

        #Se informar algo != int informa mensagem
        except ValueError:
            clear_console()
            print("----- ENTRADA INVÁLIDA! POR FAVOR, INSIRA UM NÚMERO. -----")

    return gerTipo , gerDesc

def menuSecundario(gerDesc):
    """
        Função para chamar o menu secundario

        :param: Insira o Descritivo do item selecionado no menu principal
        :return secTipo: Retorna o int para a identificação de qual o menu selecionado
        :return secDesc: Retorna o descritivo para a identificação de qual o menu selecionado
    """
    while True:
        print("\n ***** [{}] MENU DE OPERAÇÕES *****\n".format(gerDesc).upper())
        print("(1) Incluir")
        print("(2) Listar")
        print("(3) Atualizar")
        print("(4) Excluir")
        print("(9) Voltar ao menu principal")
        try:
            # Solicita que o usuário insira uma opção
            secTipo = int(input("Informe a opção desejada: "))

            # Obtém o valor correspondente ou define como "opção inválida"
            secDesc = secOpcoes.get(secTipo, "Opção inválida")

            # Verifica se a opção é válida
            if secTipo not in secOpcoes:
                clear_console()
                print("----- [{}] VOLTANDO AO MENU DE OPERAÇÕES... -----\n".format(secDesc).upper())
                continue

            # Verifica se o usuário escolheu voltar ao menu principal
            if secTipo == 9:
                clear_console()
                print("----- VOLTANDO AO MENU PRINCIPAL... -----")
                break
            
            # Se o secTipo é válido e não é 9, sai do loop
            break

        #Se informar algo != int informa mensagem    
        except ValueError:    
            clear_console()
            print("----- ENTRADA INVÁLIDA! POR FAVOR, INSIRA UM NÚMERO. -----")
        
    return secTipo, secDesc

def recuperarDadosEmMemoria(gerTipo):
    """
    Função para recuperar dados já salvos em arquivos.

    :param: Int para a identificação de qual o menu selecionado
    """
    
    global arrays_dados

    try:
        # Verifica se o tipo é válido
        if gerTipo not in gerConfig:
            print("Tipo inválido! Escolha uma opção válida.")
            return

        # Define o nome do arquivo com base no tipo
        nome_arquivo = gerConfig[gerTipo] + ".json"
        caminho_arquivo = os.path.join("Arquivos", nome_arquivo)

        # Verifica se o arquivo existe
        if not os.path.exists(caminho_arquivo):
            print(f"Sem {gerConfig[gerTipo]} recuperados: arquivo '{nome_arquivo}' não encontrado.")
            return

        # Abre e lê o conteúdo do arquivo
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

            # Verifica se o arquivo está vazio
            if not conteudo:
                print(f"Sem {gerConfig[gerTipo]} recuperados: o arquivo está vazio.")
            else:
                # Carrega os dados no array correspondente com base no tipo
                arrays_dados[gerTipo] = json.loads(conteudo)
                
                print(f"{gerConfig[gerTipo].capitalize()} recuperados com sucesso!")

    except Exception as e:
        print(f"Erro na recuperação dos {gerConfig[gerTipo]}: {e}")

def recuperarTodosDadosEmMemoria(): 
    """
    Função para recuperar TODOS os dados já salvos em arquivos.
    """

    for gerTipo in gerConfig:
        recuperarDadosEmMemoria(gerTipo)

def salvarDados(gerTipo):
    """
    Função para salvar os dados de um array em seu respectivo arquivo JSON.
    """

    # Mapeia o tipo de dado para o nome correspondente no dicionário
    nome_dado = gerConfig.get(gerTipo)

    # Verifica se o tipo é válido
    if gerTipo not in gerConfig:
        print("Tipo inválido! Escolha uma opção válida.")
        return

    # Pega os dados corretos para salvar
    dados_para_salvar = arrays_dados.get(gerTipo)

    # Define o caminho do arquivo para salvar
    caminho_arquivo = os.path.join("Arquivos", f"{nome_dado}.json")

    # Salva os dados no arquivo JSON correspondente
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados_para_salvar, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados de {nome_dado} salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados de {nome_dado}: {e}")

def gerarCodigoUnico(gerTipo):
    """
    Função para gerar um código único para o tipo de dado especificado.
    O código será o próximo número inteiro disponível com base no maior código existente.
    
    :param gerTipo: Tipo de dado para o qual o código está sendo gerado.
    :return: Código único (número inteiro)
    """
    dados = arrays_dados.get(gerTipo, [])

    if dados:
        # Encontra o maior código existente e adiciona 1
        maior_codigo = max(item["codigo"] for item in dados)
        return maior_codigo + 1
    else:
        # Se não houver dados, começa com o código 1
        return 1
    
def incluirDados(gerTipo):
    """
    Função para incluir dados (estudantes, professores, disciplinas, turmas, matrículas).

    :param gerTipo: Tipo de dado a ser incluído
    :return: Não retorna dados
    """

    global arrays_dados 
    
    # Mapeia o tipo de dado para o nome correspondente no dicionário
    nome_dado = gerConfig.get(gerTipo)

    if gerTipo == 1:  # Estudantes
        nome = input("Insira o nome do estudante: ")
        cpf = input("Insira o CPF do estudante: ")
        codigo = gerarCodigoUnico(gerTipo)  # Gera um código único para o estudante
        dado = {"codigo": codigo, "nome": nome, "cpf": cpf}

    elif gerTipo == 2:  # Professores
        nome = input("Insira o nome do professor: ")
        cpf = input("Insira o CPF do professor: ")
        codigo = gerarCodigoUnico(gerTipo)  # Gera um código único para o professor
        dado = {"codigo": codigo, "nome": nome, "cpf": cpf}

    elif gerTipo == 3:  # Disciplinas
        nome = input("Insira o nome da disciplina: ")
        codigo = gerarCodigoUnico(gerTipo)  # Gera um código único para a disciplina
        dado = {"codigo": codigo, "nome": nome}

    elif gerTipo == 4:  # Turmas
        # Validação do código do professor
        while True:
            try:
                codigo_professor = int(input("Insira o código do professor: "))
                if not any(dado['codigo'] == codigo_professor for dado in arrays_dados[2]):
                    print("Código do professor não encontrado. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Código inválido. Deve ser um número inteiro.")

        # Validação do código da disciplina
        while True:
            try:
                codigo_disciplina = int(input("Insira o código da disciplina: "))
                if not any(dado['codigo'] == codigo_disciplina for dado in arrays_dados[3]):
                    print("Código da disciplina não encontrado. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Código inválido. Deve ser um número inteiro.")

        codigo = gerarCodigoUnico(gerTipo)  # Gera um código único para a turma
        dado = {"codigo": codigo, "codigo_professor": codigo_professor, "codigo_disciplina": codigo_disciplina}

    elif gerTipo == 5:  # Matrículas
    # Validação do código da turma
        while True:
            try:
                codigo_turma = int(input("Insira o código da turma: "))
                if not any(dado['codigo'] == codigo_turma for dado in arrays_dados[4]):
                    print("Código da turma não encontrado. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Código inválido. Deve ser um número inteiro.")

        # Validação do código do estudante
        while True:
            try:
                codigo_estudante = int(input("Insira o código do estudante: "))
                if not any(dado['codigo'] == codigo_estudante for dado in arrays_dados[1]):
                    print("Código do estudante não encontrado. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Código inválido. Deve ser um número inteiro.")

        dado = {"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante}

    else:
        print("Tipo inválido! Escolha uma opção válida.")
        return

    # Adiciona o novo dado ao array correspondente
    arrays_dados[gerTipo].append(dado)

    # Limpa a tela e exibe a confirmação
    clear_console()
    print(f"*** {nome_dado.capitalize()} inserido com Sucesso! ***")
    print(dado)

    # Salva os dados no arquivo correspondente
    salvarDados(gerTipo)

    input("Pressione ENTER para continuar...")
    clear_console()

def listarDados(gerTipo):
    """
        Função para listar dados (estudantes, professores, disciplinas, turmas, matrículas).
        
        :param gerTipo: Tipo de dado a ser listado
        :return: Não retorna dados
    """
    global arrays_dados
    
    # Mapeia o tipo de dado para o nome correspondente no dicionário
    nome_dado = gerConfig.get(gerTipo)

    if not arrays_dados[gerTipo]:
        print(f"A lista de {nome_dado} está vazia.\n")
    else:
        print(f"Lista de {nome_dado}:")
        
        # Estudantes ou Professores (mesma estrutura: nome, cpf)
        if gerTipo in [1, 2]:
            for dado in arrays_dados[gerTipo]:
                print(f"Código: {dado['codigo']}, Nome: {dado['nome']}, CPF: {dado['cpf']}")
        
        # Disciplinas (apenas nome)
        elif gerTipo == 3:
            for dado in arrays_dados[gerTipo]:
                print(f"Código: {dado['codigo']}, Nome: {dado['nome']}")
        
        # Turmas (código do professor e da disciplina)
        elif gerTipo == 4:
            for dado in arrays_dados[gerTipo]:
                print(f"Código: {dado['codigo']}, Código Professor: {dado['codigo_professor']}, Código Disciplina: {dado['codigo_disciplina']}")
        
        # Matrículas (código da turma e do estudante)
        elif gerTipo == 5:
            for dado in arrays_dados[gerTipo]:
                print(f"Código Turma: {dado['codigo_turma']}, Código Estudante: {dado['codigo_estudante']}")
    
    input("Pressione ENTER para retornar ao Menu...")
    clear_console()

def alterarDados(gerTipo, secDesc):
    """
    Função genérica para alterar dados (estudantes, professores, disciplinas, turmas, matrículas).

    :param gerTipo: Tipo de dado a ser alterado (1-Estudantes, 2-Professores, 3-Disciplinas, 4-Turmas, 5-Matrículas)
    :param secDesc: Descritivo do menu secundário
    :return: Não retorna dados
    """
    global arrays_dados

    # Recupera o nome descritivo do tipo de dado a partir de gerOpcoes
    nome_dado = gerOpcoes.get(gerTipo)

    # Verifica se a lista correspondente ao tipo de dado está vazia
    if not arrays_dados[gerTipo]:
        print(f"A lista de {nome_dado} está vazia.\n")
        input("Pressione ENTER para continuar...")
        clear_console()
    else:
        while True:
            try:
                # Insere o código do dado a ser editado
                codigo_edicao = int(input(f"Insira o Código do(a) {nome_dado} que será editado(a): "))

                # Procura o dado com o código informado
                dado_encontrado = buscarPorCodigo(gerTipo, codigo_edicao)

                if dado_encontrado:
                    # Armazena os dados antigos para comparação posterior
                    dados_anteriores = dado_encontrado.copy()

                    # Solicita atualização dos campos, dependendo do tipo de dado
                    if gerTipo in [1, 2]:  # Estudantes ou Professores (Nome e CPF)
                        alterarNomeCpf(dado_encontrado, nome_dado)
                    elif gerTipo == 3:  # Disciplinas (Apenas Nome)
                        alterarNome(dado_encontrado, nome_dado)
                    elif gerTipo == 4:  # Turmas (Professores e Disciplinas)
                        alterarTurma(dado_encontrado)
                    elif gerTipo == 5:  # Matrículas (Turmas)
                        alterarMatricula(dado_encontrado)

                    # Exibe os dados anteriores e os dados atualizados
                    clear_console()
                    print("\nDados anteriores:")
                    for chave, valor in dados_anteriores.items():
                        print(f"{chave.capitalize()}: {valor}")

                    print("\nDados atualizados:")
                    for chave, valor in dado_encontrado.items():
                        print(f"{chave.capitalize()}: {valor}")

                    print(f"\n*** {nome_dado.capitalize()} com código {codigo_edicao} atualizado com sucesso! ***")
                    salvarDados(gerTipo)
                    input("Pressione ENTER para continuar...")
                    clear_console()
                    break
                else:
                    clear_console()
                    print(f"*** Nenhum(a) {nome_dado} encontrado(a) com o código {codigo_edicao}. ***")
                    input("Pressione ENTER para continuar...")
                    clear_console()

            except ValueError:
                clear_console()
                print("----- ENTRADA INVÁLIDA! POR FAVOR, INSIRA UM NÚMERO. -----")
                input("Pressione ENTER para continuar...")
                clear_console()

def alterarNomeCpf(dado, gerTipo, tipo_dado):
    """
    Função para alterar nome e CPF de estudantes ou professores.
    """
    # Altera o código do estudante ou professor
    alterarCodigo(dado, gerTipo, tipo_dado)
    
    novo_nome = input(f"Insira o novo nome (ou pressione ENTER para manter '{dado['nome']}'): ")
    novo_cpf = input(f"Insira o novo CPF (ou pressione ENTER para manter '{dado['cpf']}'): ")

    if novo_nome:
        dado['nome'] = novo_nome
    if novo_cpf:
        dado['cpf'] = novo_cpf

def alterarTurma(dado):
    """
    Função para alterar os códigos de professor e disciplina de uma turma.
    """
    # Altera o código da turma
    alterarCodigo(dado, 4, "turma")

    # Validação do código do professor
    while True:
        try:
            codigo_professor = int(input(f"Insira o novo código do professor (ou ENTER para manter '{dado['codigo_professor']}'): "))
            if not any(professor['codigo'] == codigo_professor for professor in arrays_dados[2]):
                print("Código do professor não encontrado. Tente novamente.")
                continue
            dado['codigo_professor'] = codigo_professor
            break
        except ValueError:
            print("Código inválido. Deve ser um número inteiro.")

    # Validação do código da disciplina
    while True:
        try:
            codigo_disciplina = int(input(f"Insira o novo código da disciplina (ou ENTER para manter '{dado['codigo_disciplina']}'): "))
            if not any(disciplina['codigo'] == codigo_disciplina for disciplina in arrays_dados[3]):
                print("Código da disciplina não encontrado. Tente novamente.")
                continue
            dado['codigo_disciplina'] = codigo_disciplina
            break
        except ValueError:
            print("Código inválido. Deve ser um número inteiro.")
            
def verificarCodigoExistente(gerTipo, codigo):
    """
    Verifica se um código já está em uso no tipo de dado especificado.
    
    :param gerTipo: Tipo de dado a ser verificado (1 para estudantes, 2 para professores, etc.)
    :param codigo: Código a ser verificado
    :return: True se o código já estiver em uso, False caso contrário
    """
    return any(dado['codigo'] == codigo for dado in arrays_dados[gerTipo])

def alterarCodigo(dado, gerTipo, tipo_dado):
    """
    Função para alterar o código de qualquer tipo de dado (ex: matrícula, turma, professor).
    
    :param dado: O dado que será alterado (dicionário com chave 'codigo').
    :param gerTipo: O tipo de dado que está sendo editado (para verificar existência de códigos).
    :param tipo_dado: Descrição do tipo de dado (para mensagens).
    :return: Não retorna dados, apenas altera o código no dicionário 'dado' se validado.
    """
    novo_codigo = input(f"Insira o novo código do(a) {tipo_dado} (ou pressione ENTER para manter '{dado['codigo']}'): ")
    
    while novo_codigo:
        try:
            novo_codigo = int(novo_codigo)
            if verificarCodigoExistente(gerTipo, novo_codigo):
                print(f"Código já existente para {tipo_dado}! Tente novamente.")
                novo_codigo = input(f"Insira o novo código do(a) {tipo_dado} (ou pressione ENTER para manter '{dado['codigo']}'): ")
            else:
                dado['codigo'] = novo_codigo
                break
        except ValueError:
            print("Código inválido. Deve ser um número inteiro.")
            novo_codigo = input(f"Insira o novo código do(a) {tipo_dado} (ou pressione ENTER para manter '{dado['codigo']}'): ")

def buscarPorCodigo(gerTipo, codigo):
    """
    Função para buscar um dado pelo código na lista de dados.

    :param gerTipo: Tipo de dado (estudantes, professores, etc.)
    :param codigo: Código do dado a ser buscado
    :return: O dado encontrado ou None se não for encontrado
    """
    for dado in arrays_dados[gerTipo]:
        if dado['codigo'] == codigo:
            return dado
    return None

def excluirDados(gerTipo, secDesc):
    """
    Função para excluir dados (estudantes, professores, disciplinas, turmas, matrículas).

    :param gerTipo: Tipo de dado a ser excluído
    :param secDesc: Descritivo do menu secundário
    :return: Não retorna dados
    """
    global arrays_dados

    # Recupera o nome descritivo do tipo de dado a partir de gerOpcoes
    nome_dado = gerOpcoes.get(gerTipo)

    # Verifica se a lista correspondente ao tipo de dado está vazia
    if not arrays_dados[gerTipo]:
        print(f"A lista de {nome_dado} está vazia.\n")
        input("Pressione ENTER para continuar...")
        clear_console()
    else:
        while True:
            try:
                # Solicita o código do dado a ser excluído
                codigo_exclusao = int(input(f"Insira o código do(a) {nome_dado} que será excluído(a): "))

                # Procura o dado com o código informado
                dado_encontrado = None
                for dado in arrays_dados[gerTipo]:
                    if dado["codigo"] == codigo_exclusao:
                        dado_encontrado = dado
                        break

                if dado_encontrado:
                    clear_console()
                    arrays_dados[gerTipo].remove(dado_encontrado)
                    print(f"*** {nome_dado.capitalize()} com código {codigo_exclusao} excluído com sucesso! ***")
                    salvarDados(gerTipo)
                    input("Pressione ENTER para continuar...")
                    clear_console()
                    break
                else:
                    # Informa caso não tenha o dado com o código informado
                    clear_console()
                    print(f"*** Nenhum(a) {nome_dado} encontrado(a) com o código {codigo_exclusao}. ***")
                    input("Pressione ENTER para continuar...")
                    clear_console()
                    print(f"----- {secDesc} {nome_dado} -----\n".upper())

            # Trata o erro caso o usuário não informe um número inteiro
            except ValueError:
                print("----- ENTRADA INVÁLIDA! POR FAVOR, INSIRA UM NÚMERO. -----")
                input("Pressione ENTER para continuar...")
                clear_console()
                print(f"----- {secDesc} {nome_dado} -----\n".upper())