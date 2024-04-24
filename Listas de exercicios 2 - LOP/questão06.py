categoriaInformada = int(input())

if categoriaInformada == 1:
    precoDoProduto = 10
    print("O preço do produto é: R$ {:.2f}".format(precoDoProduto))
elif categoriaInformada == 2:
    precoDoProduto = 18
    print("O preço do produto é: R$ {:.2f}".format(precoDoProduto))
elif categoriaInformada == 3:
    precoDoProduto = 23
    print("O preço do produto é: R$ {:.2f}".format(precoDoProduto))
elif categoriaInformada == 4:
    precoDoProduto = 31
    print("O preço do produto é: R$ {:.2f}".format(precoDoProduto))
else:
    print("O produto não existe.")

