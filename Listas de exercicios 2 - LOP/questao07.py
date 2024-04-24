numero1 = int(input())
numero2 = int(input())
operacao = input()

if operacao == "+":
    print("A soma é: {}".format(numero1 + numero2))
elif operacao == "-":
    print("A subtração é: {}".format(numero1 - numero2))
elif operacao == "*":
    print("A multiplicação é: {}".format(numero1 * numero2))
elif operacao == "/":
    print("A divisão é: {}".format(numero1 / numero2))