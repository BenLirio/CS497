import numpy as np

def t(As):
    if len(As) == 1:
        return As[0]
    hd, *tl = As
    return np.kron(hd, t(tl))

def gen_CZ(a, b, n):
    M = np.eye(1<<n)
    for i in range(1<<n):
        if i & ((1<<a) | (1<<b)) == ((1<<a) | (1<<b)):
            M[i, i] = -1
    return M

CZ = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, -1]])

I = np.array([[1, 0],
              [0, 1]])
H = np.array([[1, 1],
              [1, -1]]) / np.sqrt(2)

Z = np.array([[1, 0],
              [0, -1]])

PS = t([H, H]) @ t([Z, Z]) @ CZ @ t([H, H])

print()
print(gen_CZ(0, 2, 3) @ gen_CZ(0, 1, 3))

