from utils import clear_console
from functions import *

# Teste
"""
estudante = {"codigo": 1, "nome": 1, "cpf": 1}
estudantes.append(estudante)
estudante = {"codigo": 2, "nome": 2, "cpf": 2}
estudantes.append(estudante)
estudante = {"codigo": 3, "nome": 3, "cpf": 3}
estudantes.append(estudante)
"""

## Main App ##
clear_console()
inicio()

while True:

    #Chama o menu principal e obtem o numero e descritivo do menu selecionado
    gerTipo, gerDesc = menuPrincipal()

    if gerTipo == 9:
        break  # Sai do loop externo

    clear_console()    
    # Estrutura menu secundário
    while True:
        
        #Chama o menu secundario e obtem o numero e descritivo do menu selecionado
        secTipo, secDesc = menuSecundario(gerDesc)

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
                    case 1:
                        incluirEstudantes()   
                    case 2:
                        listarEstudantes()    
                    case 3:
                        alterarEstudantes(gerDesc, secDesc)
                    case 4:
                        excluirEstudantes(gerDesc, secDesc)
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