advinhe = 31
tentativa = 0
while tentativa != advinhe:
    tentativa = int(input("digite o numero entre 1 a 100: "))
    if tentativa > advinhe:
        print("muito alto")
    elif tentativa < advinhe:
        print("muito baixo")
    else:
        print("acertou")