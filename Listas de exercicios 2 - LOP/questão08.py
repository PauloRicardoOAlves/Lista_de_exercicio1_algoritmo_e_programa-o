valorDaCasa = float(input())
salario = float(input())
anosDeEmprestimo = int(input())

prestacao = valorDaCasa / (anosDeEmprestimo * 12)
margemSalario = salario * 0.3

print("prestação: {}, margemSalario: {}".format(prestacao, margemSalario))

if prestacao <= margemSalario:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo não aprovado!")