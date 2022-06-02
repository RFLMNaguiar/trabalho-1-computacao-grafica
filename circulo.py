def circulo(x_do_centro: int, y_do_centro: int, raio: int) -> list:
    """
    Função que cria os pontos discretos de um círculo.
    :param x_do_centro: posição horizontal do centro do circulo.
    :param y_do_centro: posição vertical do centro do círculo.
    :param raio: raio do círculo.
    :return: lista com pontos do círculo.
    """
    x = 0
    y = raio
    erro = -raio

    pixels = [[x, y], [y, x], [y, -x], [x, -y], [-x, -y], [-y, -x], [-y, x], [-x, y]]

    while x <= y:
        erro = erro + (2 * x + 1)
        x = x + 1
        if erro >= 0:
            erro = erro + (2 - 2 * y)
            y = y - 1
        pixels.append([x, y])
        pixels.append([y, x])
        pixels.append([y, -x])
        pixels.append([x, -y])
        pixels.append([-x, -y])
        pixels.append([-y, -x])
        pixels.append([-y, x])
        pixels.append([-x, y])

    for i in range(len(pixels)):
        pixels[i][0] += x_do_centro
        pixels[i][1] += y_do_centro

    return pixels

