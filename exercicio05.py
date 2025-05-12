soma = 0
for x in range(1,6):
    num = float(input(f"digite a {x} nota: "))
    soma += num

media = soma/5
if media >= 7 and media < 10:
    print("aprovado!")
elif media <= 4:
    print("reprovado")
elif media > 4 and media < 7:
    print("recuperacao")
else:
    print("numero invalido")
print(f"{media}")
