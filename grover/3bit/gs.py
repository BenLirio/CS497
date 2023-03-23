import numpy as np


def tensor(lst):
  hd, *tl = lst
  if not tl:
    return hd
  return np.kron(hd, tensor(tl))

A = np.eye(2)
H = np.array([
    [1, 1],
    [1, -1]
]) / np.sqrt(2)

X = np.array([
  [0, 1],
  [1, 0]
])

I = np.eye(2)

CNOT = np.array([
  [1, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 1],
  [0, 0, 1, 0]
])
O = np.eye(2**4)
O[(2**4)-1, (2**4)-1] = 0
O[(2**4)-2, (2**4)-2] = 0
O[(2**4)-1, (2**4)-2] = 1
O[(2**4)-2, (2**4)-1] = 1
t0 = tensor([
  X,
  X,
  I,
  I
])

O = t0 @ O @ t0

ket = lambda x: np.array([[1-x], [x]])
zero = lambda n: tensor([ket(0)]*n)


s = tensor([
  ket(0),
  ket(0),
  ket(0),
  ket(1),
])


phase_shift = 2 * (zero(3) @ zero(3).T) - np.eye(2**3)

G0 = tensor([H,H,H,I])
G1 = tensor([phase_shift, I])
G2 = tensor([H,H,H,I])

G = G2 @ G1 @ G0 @ O

prologue = tensor([H,H,H,H])
epilogue = tensor([I,I,I,H])

out = epilogue @ G @ G @ prologue @ s
print(np.round(out, 2))

