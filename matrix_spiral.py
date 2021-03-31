try:
    n = int(input("Введите ранг матрицы: "))
    if n == 0:
        print("Ранг должен быть больше 0")
        exit(0)
except ValueError:
    print("Ранг - это целочисленное значение больше нуля")
    exit(0)
matrix = [[0] * n for i in range(0, n)]
element = 1
el_range = 0
matrix[n // 2][n // 2] = n * n
for x in range(n // 2):
    for i in range(n - el_range):
        matrix[x][i + x] = element
        element += 1
    for i in range(x + 1, n - x):
        matrix[i][-x - 1] = element
        element += 1
    for i in range(x + 1, n - x):
        matrix[-x - 1][-i - 1] = element
        element += 1
    for i in range(x + 1, n - (x + 1)):
        matrix[-i - 1][x] = element
        element += 1
    el_range += 2
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end="\t")
    print()
