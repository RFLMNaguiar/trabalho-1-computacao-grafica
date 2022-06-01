m = [[1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 1, 1, 0, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1]]

m2 = [[1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [1, 1, 1, 0, 0],
      [1, 1, 1, 1, 1]]

m3 = [[1, 0, 0, 0, 0], [1, 0, 1, 0, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]

delta_y = 1
delta_x = 1

print("Você está fazendo uma transformação.")
x1 = int(input("Digite x inicial do bounding box:"))
y1 = int(input("Digite y inicial do bounding box:"))
x2 = int(input("Digite x final do bounding box:"))
y2 = int(input("Digite y final do bounding box:"))

coordenadas_x = [x1, x2]
coordenadas_y = [y1, y2]

x_max = max(coordenadas_x)
x_min = min(coordenadas_x)
y_max = max(coordenadas_y)
y_min = min(coordenadas_y)

print(x_min, y_min)
print(x_max, y_max)

if delta_y > 0:
    for i in range(y_min, y_max + 1):
        for j in range(x_min, x_max + 1):
            if i - delta_y >= 0:
                m[i - delta_y][j] = m[i][j]
                m[i][j] = 0

if delta_y < 0:
    for i in range(y_max, y_min, -1):
        for j in range(x_min, x_max + 1):
            if i + delta_y <= len(m[i]):
                m[i][j] = m[i + delta_y][j]
                m[i + delta_y][j] = 0

if delta_x < 0:
    for i in range(y_min, y_max + 1):
        for j in range(x_min, x_max + 1):
            if j - delta_x < len(m[i]):
                m[i][j] = m[i][j - delta_x]

if delta_x > 0:
    for i in range(y_min, y_max + 1):
        for j in range(x_max, x_min - 1, -1):
            if j + delta_x < len(m[i]):
                m[i][j + delta_x] = m[i][j]
                m[i][j] = 0

print(m)
print(m == m3)
