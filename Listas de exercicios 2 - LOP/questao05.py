minutos = int(input())
precoTotal = 0

if minutos < 200:
    precoTotal = minutos * 0.2
elif minutos <= 400:
    precoTotal = minutos * 0.18
else:
    precoTotal = minutos * 0.15

print("Você vai pagar este mês: R$ {}".format(precoTotal)) 