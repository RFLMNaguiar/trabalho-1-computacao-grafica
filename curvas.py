import bresenham

def pontos_bezier(grau_bezier: int, pontos_de_controle: list, t: float) -> list:
    """
    :param grau_bezier:
    :param pontos_de_controle: Deve ter um número de elementos igual a grau_bezier + 1
    :param t: Deve estar entre 0 e 1
    :return: Um ponto único da curva, o ponto varia conforme t muda.
    """
    pontos = []
    for i in range(grau_bezier):
        pontos.append(pontos_de_controle[i])

    for r in range(grau_bezier):
        for i in range(grau_bezier - r):
            pontos[i] = (1 - t) * pontos[i] + t * pontos[i + 1]  # interpolações lineares

    return pontos[0]

def desenha_curva():
    return None
