import numpy as np


def bezier(grau_bezier: int, pontos_de_controle: list, t: float) -> list:
    """
    :param grau_bezier:
    :param pontos_de_controle: Deve ter um número de elementos igual a grau_bezier + 1
    :param t: Deve estar entre 0 e 1
    :return pontos[0]: Um ponto único da curva, o ponto varia conforme t muda.
    """
    pontos = []
    for i in range(grau_bezier + 1):
        pontos.append(pontos_de_controle[i])

    pontos = np.array(pontos)
    pontos = pontos.astype(float)

    for r in range(grau_bezier):
        for i in range(grau_bezier - r):
            pontos[i] = (1 - t) * pontos[i] + t * pontos[i + 1]  # interpolações lineares
            pontos = np.ceil(pontos)
            pontos = pontos.astype(int)

    pontos = pontos.tolist()

    return pontos[0]



t = 0.0  # Passos de Bezier
# 24 é o número de pontos para fazer a curva
while t < 1.0:
    ponto_1 = bezier(2, [[1, 1], [2, 4], [3, 9]], t)
    ponto_2 = bezier(2, [[1, 1], [2, 4], [3, 9]], t + (1 / 6))
    t += (1 / 6)

