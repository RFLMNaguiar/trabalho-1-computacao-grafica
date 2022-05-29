import tkinter

## parametros iniciais
tamanhoTela = 600
tamanhoPixel = int(tamanhoTela / 50)
numeroPixels = tamanhoTela/tamanhoPixel

## criar o canvas utilizando o tkinter
master = tkinter.Tk()
tela = tkinter.Canvas(master, width=tamanhoTela, height=tamanhoTela)
tela.pack()


## função que cria a grade
def CriarTemplate():
    aux = int(tamanhoTela / 2) + (tamanhoPixel / 2)

    for x in range(0, tamanhoTela, tamanhoPixel):  # linhas horizontais
        tela.create_line(x, 0, x, tamanhoTela, fill='#808080')

    for y in range(0, tamanhoTela, tamanhoPixel):  # linhas verticais
        tela.create_line(0, y, tamanhoTela, y, fill='#808080')

    tela.create_line(0, aux - tamanhoPixel, tamanhoTela, aux - tamanhoPixel, fill="#f00")  # linha central - horizontal
    tela.create_line(aux, 0, aux, tamanhoTela, fill="#f00")  # linha central - vertical


def ConverterCoordenadas(x, y):  # converter coordenadas para o sistema de grade
    real_x = int((tamanhoPixel * x) + (tamanhoTela / 2)) # real_x = x + 25
    real_y = int((tamanhoTela / 2) - (tamanhoPixel * y)) # real_y = 25 - y

    return real_x, real_y


def DesenharPixel(x, y, cor):  # desenha um pixel na grade
    x1, y1 = ConverterCoordenadas(x, y)
    tela.create_rectangle(x1, y1, x1 + tamanhoPixel, y1 - tamanhoPixel, fill=cor)