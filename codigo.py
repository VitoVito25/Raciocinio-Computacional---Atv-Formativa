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

        #Informa a abertura do segundo menu
        clear_console()
        print("----- {} {} -----\n".format(secDesc, gerDesc).upper())

        #Operações de fato
        match secTipo:
            case 1:
                print("Incluir operação")
            case 2:
                print("Listar operação")
            case 3:
                print("Atualizar operação")
            case 4:
                print("Excluir operação")