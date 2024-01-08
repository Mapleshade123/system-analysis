import math
import numpy


def task():
    n = 6
    matrix = [[0 for _ in range(n * n + 1)] for _ in range(n * 2 + 1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            matrix[a + b][a * b] += 1

    p = [[x / (n * n) for x in row] for row in matrix]
    h = [[0 if pij == 0 else -pij * math.log2(pij) for pij in row] for row in p]
    Hab = sum(map(sum, h))
    p2 = [[0 if sum(row) == 0 else mij / sum(row) for mij in row] for row in matrix]
    h2 = [[0 if pij == 0 else -pij * math.log2(pij) for pij in row] for row in p2]
    HaB = 0.0

    for i in range(len(p2)):
        HaB += sum(h2[i]) * sum(p[i])

    Ha = Hab - HaB
    matrix_t = numpy.transpose(matrix)
    p = [[x / (n * n) for x in row] for row in matrix_t]
    h = [0 if sum(row) == 0 else -sum(row) * math.log2(sum(row)) for row in p]
    Hb = sum(h)
    ans = [Hab, Ha, Hb, HaB, Hb - HaB]

    return [round(x, 2) for x in ans]


if __name__ == '__main__':
    print(task())
