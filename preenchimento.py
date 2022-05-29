def preenchimento_recursivo(x, y, matriz, cor, pontos=[]):
    if matriz[y][x] != cor:
        matriz[y][x] = cor
        pontos.append([x, y])
        preenchimento_recursivo(x + 1, y, matriz, cor, pontos)
        preenchimento_recursivo(x - 1, y, matriz, cor, pontos)
        preenchimento_recursivo(x, y + 1, matriz, cor, pontos)
        preenchimento_recursivo(x, y - 1, matriz, cor, pontos)
    return pontos
