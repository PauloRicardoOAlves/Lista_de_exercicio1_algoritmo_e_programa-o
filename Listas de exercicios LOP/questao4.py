numero = int(input())
binario = 0
saida =[]

if 10 <= numero <= 20:
    binario = bin(numero)
    binario = binario.split("0b")[-1]
    for i in binario:
        saida.append(i) 
    print(saida)
else:
    print("O número inserido não está dentro do intervalo permitido.")



