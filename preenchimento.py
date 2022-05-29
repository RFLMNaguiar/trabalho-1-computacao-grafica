def preenchimento_recursivo(x, y, matriz, cor, cor_selecionada=-1):
    if cor_selecionada == -1:
        cor_selecionada = matriz[x][y]

    if len(matriz) > x > -1 and len(matriz[x]) > y > -1:
        if matriz[x][y] == cor_selecionada:
            matriz[x][y] = cor
            preenchimento_recursivo(x + 1, y, matriz, cor, cor_selecionada)
            preenchimento_recursivo(x - 1, y, matriz, cor, cor_selecionada)
            preenchimento_recursivo(x, y + 1, matriz, cor, cor_selecionada)
            preenchimento_recursivo(x, y - 1, matriz, cor, cor_selecionada)
