# Estrutura menu principal
print("------ MENU PRINCIPAL ------\n")
print("(1) Gerenciar Estudantes")
print("(2) Gerenciar Professores")
print("(3) Gerenciar Disciplinas")
print("(4) Gerenciar Turmas")
print("(5) Gerenciar Matriculas")
print("(9) Sair")

# Solicita que o usuário insira uma opção
gerTipo = int(input("Informe a opção desejada: "))


# Dicionário para mapear opções a descrições menu principal
gerOpcoes = {
    1: "Estudantes",
    2: "Professores",
    3: "Disciplinas",
    4: "Turmas",
    5: "Matriculas",
    9: "Sair"
}

# Obtém o valor correspondente ou define como "opção inválida"
gerDesc = gerOpcoes.get(gerTipo, "Opção inválida")

# Verifica se a opção é inválida
if gerTipo < 1 or (gerTipo > 5 and gerTipo != 9):
    print("----- [{}] VOLTANDO AO MENU PRINCIPAL... -----\n".format(gerDesc).upper())

# Estrutura menu secundario
print("\n ***** [{}] MENU DE OPERAÇÕES *****\n".format(gerDesc).upper())
print("(1) Incluir")
print("(2) Listar")
print("(3) Atualizar")
print("(4) Excluir")
print("(9) Voltar ao menu principal")

# Solicita que o usuário insira uma opção
secTipo = int(input("Informe a opção desejada: "))

# Dicionário para mapear opções a descrições menu secundario
secOpcoes = {
    1: "Incluir",
    2: "Listar",
    3: "Atualizar",
    4: "Excluir",
    9: "Sair"
}

# Obtém o valor correspondente ou define como "opção inválida"
secDesc = secOpcoes.get(secTipo, "Opção inválida")

#Informando Seleção
print("\n ***** [{}] *****\n".format(secDesc).upper())