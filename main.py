from utils import clear_console
from functions import *

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

        match secTipo:
            case 1:
                incluirDados(gerTipo)   
            case 2:
                listarDados(gerTipo)    
            case 3:
                alterarDados(gerTipo)
            case 4:
                excluirDados(gerTipo, secDesc)
