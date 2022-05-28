def bresenham(ponto_inicial, ponto_final):
    # REFLEXÃO:
    m = (ponto_final[1] - ponto_inicial[1]) / (ponto_final[0] - ponto_inicial[0])

    troca = ['NENHUMA']
    if m > 1 or m < -1:
        ponto_inicial[0], ponto_inicial[1] = ponto_inicial[1], ponto_inicial[0]
        ponto_final[0], ponto_final[1] = ponto_final[1], ponto_final[0]
        troca.append('XY')
    if ponto_inicial[0] > ponto_final[0]:
        ponto_inicial[0], ponto_final[0] = -ponto_inicial[0], -ponto_final[0]
        troca.append('X')
    if ponto_inicial[1] > ponto_final[1]:
        ponto_inicial[1], ponto_final[1] = -ponto_inicial[1], -ponto_final[1]
        troca.append('Y')

    # BRESENHAM:
    coeficiente_angular = (ponto_final[1] - ponto_inicial[1]) / (ponto_final[0] - ponto_inicial[0])
    erro = coeficiente_angular - 0.5
    y = ponto_inicial[1]

    pixels = [ponto_inicial]

    for i in range(ponto_inicial[0] + 1, ponto_final[0]):
        if erro > 0:
            erro = erro - 1
            y += 1
        pixels.append([i, y])
        erro = erro + coeficiente_angular

    pixels.append(ponto_final)

    # DEREFLEXÃO:
    if "Y" in troca:
        for i in range(len(pixels)):
            pixels[i] = [pixels[i][0], -pixels[i][1]]
    if "X" in troca:
        for i in range(len(pixels)):
            pixels[i] = [-pixels[i][0], pixels[i][1]]
    if "XY" in troca:
        for i in range(len(pixels)):
            pixels[i] = [pixels[i][1], pixels[i][0]]

    return pixels




