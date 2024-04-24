entrada = input().split()
condicao = False

usuario1, senha1, usuario2, senha2, usuario3, senha3, usuarioInformado, senhaInformada = entrada

usuarios_senhas = [[usuario1, senha1],[usuario2, senha2],[usuario3, senha3]]

for i in usuarios_senhas:
    if usuarioInformado and senhaInformada in i:
        condicao = True

if(condicao):
    print("Login bem-sucedido! Bem-vindo, {}.".format(usuarioInformado))
else:
    print("Acesso negado. Credenciais inválidas.")
