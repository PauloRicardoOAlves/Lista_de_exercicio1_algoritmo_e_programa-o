distancia = float(input())
precoPassagem = 0

if distancia <= 200:
    precoPassagem = distancia * 0.5
else:
    precoPassagem = distancia * 0.45

print("Sua passagem custa: R$ {:.2f}".format(precoPassagem))