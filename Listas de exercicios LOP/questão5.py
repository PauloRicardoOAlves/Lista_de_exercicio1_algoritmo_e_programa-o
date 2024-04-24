coordenadas = input().split()

xmin, ymin, xmax, ymax, x, y= coordenadas

if xmin <= x <= xmax and ymin <= y <= ymax:
    if xmin == x or xmax == x or ymin == y or ymax == y:
        print("O ponto está tocando a borda do retângulo.")
    else:
        print("O ponto está dentro do retângulo.")
else:
    print("O ponto está fora do retângulo.")



