def senha_forte(senha):
    tem_8_caracteres = len(senha) >= 8
    tem_numero = any(char.isdigit() for char in senha)
    return tem_8_caracteres and tem_numero

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    if senha_forte(senha):
        print("Senha forte! ✅")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e conter pelo menos um número.\n")
