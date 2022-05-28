m = [[1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 1, 1, 0, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1]]

delta_y = 1
delta_x = 1

x1, y1 = 1, 1
x2, y2 = 3, 3

if delta_y > 0:
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i-delta_y >= 0:
                m[i-delta_y][j] = m[i][j]
                m[i][j] = 0

if delta_y < 0:
    for i in range(len(m) - 1, 0, -1):
        for j in range(len(m[i])):
            if i+delta_y <= len(m[i]):
                m[i][j] = m[i+delta_y][j]
                m[i+delta_y][j] = 0

'''if delta_x < 0:
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j - delta_x < len(m[i]):
                m[i][j] = m[i][j - delta_x]'''


'''if delta_x > 0:
    for i in range(len(m)):
        for j in range(len(m[i]) - 1, -1, -1):
            if j + delta_x < len(m[i]):
                m[i][j + delta_x] = m[i][j]
                m[i][j] = 0'''

print(m)
