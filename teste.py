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

delta_y = -1
delta_x = 1

x1, y1 = 1, 1
x2, y2 = 3, 3

if delta_y > 0:
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if i-delta_y >= 0:
                m[i-delta_y][j] = m[i][j]
                m[i][j] = 0

if delta_y < 0:
    for i in range(y2, y1, -1):
        for j in range(x1, x2+1):
            if i+delta_y <= len(m[i]):
                m[i][j] = m[i+delta_y][j]
                m[i+delta_y][j] = 0

if delta_x < 0:
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if j - delta_x < len(m[i]):
                m[i][j] = m[i][j - delta_x]


if delta_x > 0:
    for i in range(y1, y2+1):
        for j in range(x2, x1 - 1, -1):
            if j + delta_x < len(m[i]):
                m[i][j + delta_x] = m[i][j]
                m[i][j] = 0

print(m)
print(m == m2)