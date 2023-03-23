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

n = 8

O = np.eye(2**(n+1))
O[(2**(n+1))-1, (2**(n+1))-1] = 0
O[(2**(n+1))-2, (2**(n+1))-2] = 0
O[(2**(n+1))-1, (2**(n+1))-2] = 1
O[(2**(n+1))-2, (2**(n+1))-1] = 1
t0 = tensor([I]*n + [I])

O = t0 @ O @ t0

ket = lambda x: np.array([[1-x], [x]])
zero = lambda n: tensor([ket(0)]*n)


s = tensor(
  [ket(0)]*n
  +[ket(1)]
)


phase_shift = 2 * (zero(n) @ zero(n).T) - np.eye(2**n)

G0 = tensor([H]*n+[I])
G1 = tensor([phase_shift, I])
G2 = tensor([H]*n+[I])

G = G2 @ G1 @ G0 @ O

prologue = tensor([H]*(n+1))
epilogue = tensor([I]*n+[H])

gates = [prologue] + [G]*3 + [epilogue]
gates.reverse()
for g in gates:
  s = g @ s
print(np.round(s, 2))

