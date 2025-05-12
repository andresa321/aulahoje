senha = 1234
while senha:
    num = int(input("digite a senha: "))
    if num == senha:
        print("acesso liberado")
        break
    else:
        print("senha incorreta")