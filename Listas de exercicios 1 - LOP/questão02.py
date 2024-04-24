numero = int(input())

if 100 < numero < 1000:
    resto = numero % 5
    print("O resto da divisão de {} por 5 é {}.".format(numero, resto))
else:
    print("Por favor, insira um número inteiro positivo entre 100 e 1000.")

