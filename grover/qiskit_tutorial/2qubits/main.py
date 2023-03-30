import numpy as np

def t(As):
    if len(As) == 1:
        return As[0]
    hd, *tl = As
    return np.kron(hd, t(tl))

H = np.array([
    [1, 1],
    [1, -1]
]) / np.sqrt(2)

U_w = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, -1]])

U_0 = np.array([
    [1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, -1]])

U_s = t([H,H]) @ U_0 @ t([H,H])

ket = lambda n: np.array([
    [np.sqrt(1-n)],
    [np.sqrt(n)]])

s = t([
    ket(0),
    ket(0)
])

s = t([H, H]) @ s

s = U_w @ s

s = U_s @ s

print(s)
