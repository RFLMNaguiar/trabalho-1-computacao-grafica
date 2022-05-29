import bresenham
import circulo
import elipse
import grid
import tkinter


def colocar_nos_limites(x: int, y: int) -> tuple[int, int]:
    if x > 24:
        x = 24
    elif x < -25:
        x = -25

    if y > 24:
        y = 24
    elif y < -25:
        y = -25

    return x, y


def desenhar_com_recorte(x_reta: int, y_reta: int, matriz: list, cor: int) -> None:
    y_na_matriz, x_na_matriz = converter_coordenadas(x_na_reta, y_na_reta)
    if estah_nos_limites(x_reta, y_reta):
        matriz[x_na_matriz][y_na_matriz] = cor
        grid.DesenharPixel(x_na_reta, y_na_reta, '#f00')


def estah_nos_limites(x_reta: int, y_reta: int) -> bool:
    if (-25 <= x_reta <= 24) and (-25 <= y_reta <= 24):
        return True
    else:
        return False


def converter_coordenadas(x_reta: int, y_reta: int) -> tuple[int, int]:
    x_real = x_reta + 25
    y_real = 24 - y_reta
    return x_real, y_real


def imprimir_matriz(matriz: list) -> None:
    for linha in range(len(matriz)):
        print()
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna], end="")
    print()


def desenhar_a_matriz(matriz: list) -> None:
    grid.DesenharPixel(x_na_reta, y_na_reta, "#000")


matriz = []
cor_atual = 1
dicionario_cores = {0: "branco",
                    1: "vermelho",
                    2: "verde",
                    3: "azul",
                    4: "preto"}

for i in range(int(grid.numeroPixels)):
    matriz.append([])
    for _ in range(int(grid.numeroPixels)):
        matriz[i].append(0)

print("Bem-vindo ao trabalho prático 1!")
print("Disciplina: Computação Gráfica")
print("Aluno: Samuel Figueira Aguiar")
print("Matrícula: 201904940010")

while True:
    print(f"Cor atual: {dicionario_cores[cor_atual]}")
    print("Digite a ação que você quer executar:")
    print("0 - Mostrar o desenho feito (termina o programa).")
    print("1 - Desenhar um ponto.")
    print("2 - Desenhar uma linha.")
    print("3 - Desenhar um círculo.")
    print("4 - Desenhar uma elipse.")
    print("5 - Fazer uma transformação.")
    print("6 - Trocar a cor do pincel.")
    opcao = int(input("Opção:"))

    if opcao == 0:
        desenhar_a_matriz(matriz)
        grid.CriarTemplate()
        tkinter.mainloop()
        break
    elif opcao == 1:
        print("Você está desenhando um ponto.")
        x_na_reta = int(input("Digite a coordenada x do ponto: "))
        y_na_reta = int(input("Digite a coordenada y do ponto: "))

        print("Desenhando um ponto...")
        desenhar_com_recorte(x_na_reta, y_na_reta, matriz, cor_atual)
        print("Reta desenhado com sucesso!")

    elif opcao == 2:
        print("Você está desenhando uma reta (bresenham).")
        x1 = int(input("Digite a coordenada x do primeiro ponto: "))
        y1 = int(input("Digite a coordenada y do primeiro ponto: "))
        x2 = int(input("Digite a coordenada x do segundo ponto: "))
        y2 = int(input("Digite a coordenada y do segundo ponto: "))

        print("Desenhando uma reta...")

        pontos_da_reta = bresenham.bresenham([x1, y1], [x2, y2])
        for i in range(len(pontos_da_reta)):
            x_na_reta, y_na_reta = pontos_da_reta[i][0], pontos_da_reta[i][1]
            desenhar_com_recorte(x_na_reta, y_na_reta, matriz, cor_atual)

        print("Reta desenhada com sucesso!")
    elif opcao == 3:
        print("Você está desenhando um círculo.")
        x = int(input("Digite a coordenada x do centro: "))
        y = int(input("Digite a coordenada y do centro: "))
        r = int(input("Digite o raio do círculo: "))

        print("Desenhando um circulo...")

        pontos_do_circulo = circulo.circulo(x, y, r)
        for i in range(len(pontos_do_circulo)):
            x_na_reta, y_na_reta = pontos_do_circulo[i][0], pontos_do_circulo[i][1]
            desenhar_com_recorte(x_na_reta, y_na_reta, matriz, cor_atual)

        print("Círculo desenhado com sucesso!")

    elif opcao == 4:
        print("Você está desenhando uma elipse.")
        x = int(input("Digite a coordenada x do centro: "))
        y = int(input("Digite a coordenada y do centro: "))
        rx = int(input("Digite o raio vertical da elipse"))
        ry = int(input("Digite o raio vertical da elipse"))

        print("Desenhando a elipse...")

        pontos_da_elipse = elipse.elipse(rx, ry, x, y)
        for i in range(len(pontos_da_elipse)):
            x_na_reta, y_na_reta = pontos_da_elipse[i][0], pontos_da_elipse[i][1]
            desenhar_com_recorte(x_na_reta, y_na_reta, matriz, cor_atual)

        print("Elipse desenhada com sucesso!")
    elif opcao == 5:
        print("Você está fazendo uma transformação.")
        x1 = int(input("Digite x inicial do bounding box:"))
        y1 = int(input("Digite y inicial do bounding box:"))
        x2 = int(input("Digite x final do bounding box:"))
        y2 = int(input("Digite y final do bounding box:"))

        # Coloca os pontos do bouding box dentro dos limites.
        x1, y1 = colocar_nos_limites(x1, y1)
        x2, y2 = colocar_nos_limites(x2, y2)

        # Forma o bouding box corretamente para a iteração.
        coordenadas_x = [x1, x2]
        coordenadas_y = [y1, y2]
        x_max = max(coordenadas_x)
        x_min = min(coordenadas_x)
        y_max = max(coordenadas_y)
        y_min = min(coordenadas_y)

        print("1 - Translação.")
        print("2 - Escala.")
        print("3 - Rotação.")
        transformacao = int(input("Digite a transformação que você deseja efetuar:"))
        if transformacao == 1:
            print("Você selecionou a translação.")
            vertical_ou_horizontal = input("(V)ertical ou (H)orizontal?")
            if vertical_ou_horizontal == "H":
                delta_x = int(input("Digite a quantidade horizontal que você deseja mover:"))

                if delta_x < 0:
                    for i in range(y_min, y_max + 1):
                        for j in range(x_min, x_max + 1):
                            if j - delta_x < len(matriz[i]):
                                matriz[i][j] = matriz[i][j - delta_x]

                if delta_x > 0:
                    for i in range(y_min, y_max + 1):
                        for j in range(x_max, x_min - 1, -1):
                            if j + delta_x < len(matriz[i]):
                                matriz[i][j + delta_x] = matriz[i][j]
                                matriz[i][j] = 0

            elif vertical_ou_horizontal == "V":
                delta_y = int(input("Digite a quantidade vertical que você deseja mover:"))

                if delta_y > 0:
                    for i in range(y_min, y_max + 1):
                        for j in range(x_min, x_max + 1):
                            if i - delta_y >= 0:
                                matriz[i - delta_y][j] = matriz[i][j]
                                matriz[i][j] = 0
                if delta_y < 0:
                    for i in range(y_max, y_min, -1):
                        for j in range(x_min, x_max + 1):
                            if i + delta_y <= len(matriz[i]):
                                matriz[i][j] = matriz[i + delta_y][j]
                                matriz[i + delta_y][j] = 0

        elif transformacao == 2:
            print("Você selecionou a escala.")
            delta_x = int(input("Digite a quantidade horizontal que você deseja alterar:"))
            delta_y = int(input("Digite a quantidade vertical que você deseja alterar:"))


        elif transformacao == 3:
            print("Você selecionou a escala.")
            graus = int(input("Digite quantos graus você deseja rotacionar:"))

        else:
            print("OPÇÃO INVÁLIDA, ESCOLHA OUTRA TRANSFORMAÇÃO.")

    elif opcao == 6:
        print("Você está trocando a cor.")
        print("0 - Branco.")
        print("1 - Vermelho.")
        print("2 - Verde.")
        print("3 - Azul.")
        print("4 - Preto.")
        cor_atual = int(input("Digite a cor que você deseja selecionar: "))
        print(f"Cor selecionada: {dicionario_cores[0]}")
    else:
        print("Opção inválida!")
