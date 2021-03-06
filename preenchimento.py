def preenchimento_recursivo(x: int, y: int, matriz: list[list], cor: int, cor_selecionada=-1) -> None:
    """
    Função que preenche recursivamente uma matriz.
    :param x: localização horizontal inicial do preenchimento.
    :param y: localização vertical inicial do preenchimento.
    :param matriz: matriz a ser preenchida.
    :param cor: cor que será utilizada para preencher.
    :param cor_selecionada: cor em que o preenchimento iniciou para ser usada na recursão (NÃO USAR).
    :return:
    """
    if cor_selecionada == -1:
        cor_selecionada = matriz[x][y]

    if len(matriz) > x > -1 and len(matriz[x]) > y > -1:
        if matriz[x][y] == cor_selecionada:
            matriz[x][y] = cor
            preenchimento_recursivo(x + 1, y, matriz, cor, cor_selecionada)
            preenchimento_recursivo(x - 1, y, matriz, cor, cor_selecionada)
            preenchimento_recursivo(x, y + 1, matriz, cor, cor_selecionada)
            preenchimento_recursivo(x, y - 1, matriz, cor, cor_selecionada)
