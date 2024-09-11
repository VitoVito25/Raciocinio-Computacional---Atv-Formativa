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

def inicio():
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
                if gerTipo == 1:
                    global estudantes
                    estudantes = json.loads(conteudo)
                elif gerTipo == 2:
                    global professores
                    professores = json.loads(conteudo)
                elif gerTipo == 3:
                    global disciplinas
                    disciplinas = json.loads(conteudo)
                elif gerTipo == 4:
                    global turmas
                    turmas = json.loads(conteudo)
                elif gerTipo == 5:
                    global matriculas
                    matriculas = json.loads(conteudo)
                
                print(f"{gerConfig[gerTipo].capitalize()} recuperados com sucesso!")

    except Exception as e:
        print(f"Erro na recuperação dos {gerConfig[gerTipo]}: {e}")

def recuperarTodosDadosEmMemoria(): 
    """
    Função para recuperar TODOS os dados já salvos em arquivos.
    """

    for gerTipo in gerConfig:
        recuperarDadosEmMemoria(gerTipo)

def salvarDados():
    """
        Função para salvar dados do array para o arquivo
    """
    global estudantes  # Usa o array global estudantes

    # Define o caminho do arquivo
    caminho_arquivo = os.path.join("Arquivos", "estudantes.json")

    # Salva os dados do array 'estudantes[]' no arquivo JSON (sobrescreve o arquivo)
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(estudantes, arquivo_json, ensure_ascii=False, indent=4)
        print("Dados dos estudantes salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def incluirEstudantes():
    """
        Função para incluir estudantes

        :param: Não é necessario a inclusão de parametros
        :return: Não retorna dados
    """
    nome = input("Insira o nome do estudante: ")
    cpf = input("Insira o CPF do estudante: ")
    codigo = len(estudantes) + 1  # Gera um código sequencial para o estudante
    estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    estudantes.append(estudante)

    clear_console()
    print(f"Código: {codigo}, Nome: {nome}, CPF: {cpf}")
    print("*** Estudante inserido com Sucesso! ***")
    salvarDados()
    input("Pressione ENTER para continuar...")
    clear_console()

def listarEstudantes():
    """
        Função para listar estudantes

        :param: Não é necessario a inclusão de parametros
        :return: Não retorna dados
    """
    if not estudantes:
        print("A lista de estudantes está vazia.\n")
    else:
        print("Lista de estudantes:")
        for estudante in estudantes:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")
    input("Pressione ENTER para retornar ao Menu...")
    clear_console()

def alterarEstudantes(gerDesc, secDesc):
    """
        Função para alterar estudantes

        :param gerDesc: Descritivo do menu principal
        :param secDesc: Descritivo do menu secundario
        :return: Não retorna dados
    """

    # Verifica se a lista de estudantes está vazia
    if not estudantes:
        print("A lista de estudantes está vazia.\n")
        input("Pressione ENTER para continuar...")
        clear_console()
    else:
        while True:
            try:
                # Insira o código do estudante a ser editado
                codigo_edicao = int(input("Insira o Código do Estudante que será editado: "))

                # Procura o estudante com o código informado
                estudante_encontrado = None
                for estudante in estudantes:
                    if estudante["codigo"] == codigo_edicao:
                        estudante_encontrado = estudante

                        # Armazena os dados antigos para comparação posterior
                        dados_anteriores = estudante_encontrado.copy()
                        break
                
                # Permite que o usuário atualize o nome, CPF e/ou código
                if estudante_encontrado:
                    while True:
                        #Validacao do novo codigo
                        try:
                            print(f"Estudante encontrado: Código: {estudante_encontrado['codigo']}, Nome: {estudante_encontrado['nome']}, CPF: {estudante_encontrado['cpf']}")
                            novo_codigo = input(f"Insira o novo código (ou pressione ENTER para manter '{estudante_encontrado['codigo']}'): ")
                            
                            if novo_codigo == "":  # Se o usuário pressionar ENTER, mantém o código atual
                                break
                            
                            novo_codigo = int(novo_codigo)  # Tenta converter a entrada para inteiro

                            # Verifica se o novo código já está em uso
                            codigo_existente = any(estudante['codigo'] == novo_codigo for estudante in estudantes)
                            
                            if codigo_existente:
                                print(f"*** O código {novo_codigo} já está em uso. Por favor, escolha um código diferente. ***")
                                input("Pressione ENTER para tentar novamente...")
                                clear_console()
                                print("----- {} {} -----\n".format(secDesc, gerDesc).upper())
                            else:
                                estudante_encontrado['codigo'] = novo_codigo  # Atualiza o código do estudante
                                break
                            
                        except ValueError:
                            clear_console()
                            print("----- ENTRADA INVÁLIDA! POR FAVOR, INSIRA UM NÚMERO. -----")
                            input("Pressione ENTER para tentar novamente...")
                            clear_console()
                            print("----- {} {} -----\n".format(secDesc, gerDesc).upper())                                        
                    
                    # Solicita novos Nome e CPF ou mantém os atuais se o usuário não informar nada
                    novo_nome = input(f"Insira o novo nome (ou pressione ENTER para manter '{estudante_encontrado['nome']}'): ")
                    novo_cpf = input(f"Insira o novo CPF (ou pressione ENTER para manter '{estudante_encontrado['cpf']}'): ")

                    if novo_nome:
                        estudante_encontrado['nome'] = novo_nome
                    if novo_cpf:
                        estudante_encontrado['cpf'] = novo_cpf

                    # Exibe os dados anteriores e os dados atualizados
                    clear_console()
                    print("\nDados anteriores:")
                    print(f"Código: {dados_anteriores['codigo']}, Nome: {dados_anteriores['nome']}, CPF: {dados_anteriores['cpf']}")
                    print("\nDados atualizados:")
                    print(f"Código: {estudante_encontrado['codigo']}, Nome: {estudante_encontrado['nome']}, CPF: {estudante_encontrado['cpf']}")

                    print(f"\n*** Estudante com código {codigo_edicao} atualizado com sucesso! ***")
                    salvarDados()
                    input("Pressione ENTER para continuar...")
                    clear_console()
                    break
                else:
                    # Informa caso não tenha o estudante com o código informado
                    clear_console()
                    print(f"*** Nenhum estudante encontrado com o código {codigo_edicao}. ***")
                    input("Pressione ENTER para continuar...")
                    clear_console()
                    print("----- {} {} -----\n".format(secDesc, gerDesc).upper())

            # Trata o erro caso o usuário não informe um número inteiro
            except ValueError:
                clear_console()
                print("----- ENTRADA INVÁLIDA! POR FAVOR, INSIRA UM NÚMERO. -----")
                input("Pressione ENTER para continuar...")
                clear_console()
                print("----- {} {} -----\n".format(secDesc, gerDesc).upper())


def excluirEstudantes(gerDesc, secDesc):
    """
        Função para excluir estudantes

        :param gerDesc: Descritivo do menu principal
        :param secDesc: Descritivo do menu secundario
        :return: Não retorna dados
    """
    #Verifica se a lista de Estudantes esta vazia
    if not estudantes:
        print("A lista de estudantes está vazia.\n")
        input("Pressione ENTER para continuar...")
        clear_console()
    else:
        while True:
            try:
                #Insira o codigo do estudante a ser excluido
                codigo_exclusao = int(input("Insira o Codigo do Estudante que será excluído: "))

                # Procura o estudante com o código informado
                estudante_encontrado = None
                for estudante in estudantes:
                    if estudante["codigo"] == codigo_exclusao:
                        estudante_encontrado = estudante
                        break

                if estudante_encontrado:
                    clear_console()
                    estudantes.remove(estudante_encontrado)
                    print(f"*** Estudante com código {codigo_exclusao} excluído com sucesso! ***")
                    salvarDados()
                    input("Pressione ENTER para continuar...")
                    clear_console()
                    break 
                else:
                    #Informa caso nao tenha o estudante com o codigo informado
                    clear_console()
                    print(f"*** Nenhum estudante encontrado com o código {codigo_exclusao}. ***")
                    input("Pressione ENTER para continuar...")
                    clear_console()
                    print("----- {} {} -----\n".format(secDesc, gerDesc).upper())

            #Trata o erro caso o usuario nao informe um int
            except ValueError:
                print("----- ENTRADA INVÁLIDA! POR FAVOR, INSIRA UM NÚMERO. -----")
                input("Pressione ENTER para continuar...")
                clear_console()
                print("----- {} {} -----\n".format(secDesc, gerDesc).upper())