import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')

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
                input("Pressione ENTER para continuar...")
                clear_console()
                continue

            # Verifica se o usuário escolheu sair
            if gerTipo == 9:
                clear_console()
                print("----- SAINDO DO SISTEMA... -----")
                input("Pressione ENTER para continuar...")
                break
            
            # Se o gerTipo é válido e não é 9, sai do loop
            ## Colocando delimitador por conta da solicitação da AS1
            if gerTipo == 1: 
                break
            else:
                clear_console()
                print("----- OPÇÂO EM DESENVOLVIMENTO -----")
                input("Pressione ENTER para continuar...")
                clear_console()                

        #Se informar algo != int informa mensagem
        except ValueError:
            clear_console()
            print("----- ENTRADA INVÁLIDA! POR FAVOR, INSIRA UM NÚMERO. -----")
            input("Pressione ENTER para continuar...")
            clear_console()

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
                input("Pressione ENTER para continuar...")
                clear_console()

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
                        estudantes.append(str(input("Insira o nome do estudante: ")))
                        input("Pressione ENTER para continuar...")
                        clear_console()
                        print("*** Estudante inserido com Sucesso! ***")
                    #Listar    
                    case 2:
                        if not estudantes:
                            print("Não há estudantes cadastrados. \n")
                        else:
                            print("Lista de estudantes:")
                            for estudante in estudantes:
                                print(" - {}".format(estudante))
                        input("Pressione ENTER para retornar ao Menu...")
                        clear_console()
                    case 3:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                    case 4:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
            case 2 :
                match secTipo:
                    case 1:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 2:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                    case 3:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 4:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break        
            case 3 :
                match secTipo:
                    case 1:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 2:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 3:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 4:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
            case 4 :
                match secTipo:
                    case 1:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 2:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 3:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 4:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break            
            case 5 :
                match secTipo:
                    case 1:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 2:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 3:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break
                    case 4:
                        print("----- EM DESENVOLVIMENTO -----")
                        input("Pressione ENTER para continuar...")
                        break