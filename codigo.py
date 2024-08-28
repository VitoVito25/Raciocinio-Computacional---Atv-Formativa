from utils import clear_console

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

# Estrutura de listagem de estudantes
estudantes = []


# Teste
"""
estudante = {"codigo": 1, "nome": 1, "cpf": 1}
estudantes.append(estudante)
estudante = {"codigo": 2, "nome": 2, "cpf": 2}
estudantes.append(estudante)
estudante = {"codigo": 3, "nome": 3, "cpf": 3}
estudantes.append(estudante)
"""

## Main ##
clear_console()
while True:
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

    if gerTipo == 9:
        break  # Sai do loop externo

    clear_console()    
    # Estrutura menu secundário
    while True:
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

        # Se o secTipo é válido e não é 9, loop
        if secTipo == 9:
            break  # Sai do loop externo        

        #Informa a abertura do menu
        clear_console()
        print("----- {} {} -----\n".format(secDesc, gerDesc).upper())

        match gerTipo:
            #Estudantes
            case 1 : 
                match secTipo:
                    #Incluir
                    case 1:
                        nome = input("Insira o nome do estudante: ")
                        cpf = input("Insira o CPF do estudante: ")
                        codigo = len(estudantes) + 1  # Gera um código sequencial para o estudante
                        estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
                        estudantes.append(estudante)
                        input("Pressione ENTER para continuar...")

                        clear_console()
                        print("*** Estudante inserido com Sucesso! ***")
                    #Listar    
                    case 2:
                        if not estudantes:
                            print("A lista de estudantes está vazia.\n")
                            input("Pressione ENTER para continuar...")
                        else:
                            print("Lista de estudantes:")
                            for estudante in estudantes:
                                print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")
                        input("Pressione ENTER para retornar ao Menu...")
                        clear_console()
                    #Editar    
                    case 3:
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

                    #Excluir
                    case 4:
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
                                        estudantes.remove(estudante_encontrado)
                                        print(f"*** Estudante com código {codigo_exclusao} excluído com sucesso! ***")
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
            case 2 :
                match secTipo:
                    case 1:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 2:
                        print("----- EM DESENVOLVIMENTO -----")
                    case 3:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 4:
                        print("----- EM DESENVOLVIMENTO -----")
                        break        
            case 3 :
                match secTipo:
                    case 1:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 2:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 3:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 4:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
            case 4 :
                match secTipo:
                    case 1:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 2:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 3:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 4:
                        print("----- EM DESENVOLVIMENTO -----")
                        break            
            case 5 :
                match secTipo:
                    case 1:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 2:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 3:
                        print("----- EM DESENVOLVIMENTO -----")
                        break
                    case 4:
                        print("----- EM DESENVOLVIMENTO -----")
                        break