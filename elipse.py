def elipse(raio_horizontal: int, raio_vertical: int, x_do_centro: int, y_do_centro: int) -> list:
    """
    Função que cria os pontos discretos de uma elipse.
    :param raio_horizontal: raio horizontal da elipse.
    :param raio_vertical:  raio vertical da elipse.
    :param x_do_centro: posição horizontal do centro do circulo.
    :param y_do_centro: posição vertical do centro do círculo.
    :return: lista com pontos da elipse.
    """
    raio_horizontal_ao_quadrado = raio_horizontal ** 2
    raio_vertical_ao_quadrado = raio_vertical ** 2

    x = 0
    y = raio_vertical
    pixels = []

    dx = 2 * raio_vertical_ao_quadrado * x
    dy = 2 * raio_horizontal_ao_quadrado * y

    erro = (- raio_vertical * raio_horizontal_ao_quadrado) + (raio_horizontal_ao_quadrado * 0.25)

    while dx < dy:
        pixels.append([x, y])
        pixels.append([-x, y])
        pixels.append([x, -y])
        pixels.append([-x, -y])

        x = x + 1
        erro = erro + dx + raio_vertical_ao_quadrado
        dx = dx + 2 * raio_vertical_ao_quadrado

        if erro > 0:
            y = y - 1
            erro = erro + raio_horizontal_ao_quadrado - dy
            dy = dy - 2 * raio_horizontal_ao_quadrado

        erro = raio_vertical_ao_quadrado * ((x + 0.5) * (
                    x + 0.5) + raio_horizontal_ao_quadrado * y * y - raio_horizontal_ao_quadrado * raio_vertical_ao_quadrado)

        while y >= 0:
            pixels.append([x, y])
            pixels.append([-x, y])
            pixels.append([x, -y])
            pixels.append([-x, -y])

            y = y - 1
            erro = erro + raio_horizontal_ao_quadrado - dy
            dy = dy - 2 * raio_horizontal_ao_quadrado

            if erro < 0:
                x = x + 1
                erro = erro + dx + raio_vertical_ao_quadrado
                dx = dx + 2 * raio_vertical_ao_quadrado

    for i in range(len(pixels)):
        pixels[i][0] += x_do_centro
        pixels[i][1] += y_do_centro

    return pixels
