def circulo(x_do_centro, y_do_centro, raio):
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

