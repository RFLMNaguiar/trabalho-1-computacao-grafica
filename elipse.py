def elipse(raio_horizontal, raio_vertical, x_do_centro, y_do_centro):
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
