import numpy as np

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
Toffoli = np.array([
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 1, 0]
])

def tensor(lst):
  hd, *tl = lst
  if not tl:
    return hd
  return np.kron(hd, tensor(tl))

def show(A):
  for i in range(0, len(A), 2):
    if np.round(A[i][0], 2) == -np.round(A[i+1][0],2):
      s = '+'
      m = 1
      if A[i][0] < 0:
        s = '-'
        m = -1
      print(s*(int(A[i][0]*20)*m))


ket = lambda x: np.array([[1-x], [x]])
zero = lambda n: tensor([ket(0)]*n)


s = tensor([
  ket(0),
  ket(0),
  ket(1)
])

t0 = tensor([
  X,
  I,
  I
])

O = t0 @ Toffoli @ t0

phase_shift = 2 * (zero(2) @ zero(2).T) - tensor([I, I])

G0 = tensor([H,H,I])
G1 = tensor([phase_shift, I])
G2 = tensor([H,H,I])

G = G2 @ G1 @ G0 @ O

prologue = tensor([H,H,H])
epilogue = tensor([I,I,H])

print("Prologue")
show(prologue @ s)
print("After Oracle")
show(O @ prologue @ s)
print("After G")
show(G @ prologue @ s)


# print("final")
# out = epilogue @ G @ prologue @ s
# print(np.round(out, 2))

