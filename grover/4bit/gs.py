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

n = 4

O = np.eye(2**(n+1))
O[(2**(n+1))-1, (2**(n+1))-1] = 0
O[(2**(n+1))-2, (2**(n+1))-2] = 0
O[(2**(n+1))-1, (2**(n+1))-2] = 1
O[(2**(n+1))-2, (2**(n+1))-1] = 1
t0 = tensor([X]*n + [I])

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

def show(A):
  for i in range(0, len(A), 2):
    if np.round(A[i][0], 2) == -np.round(A[i+1][0],2):
      s = '+'
      m = 1
      if A[i][0] < 0:
        s = '-'
        m = -1
      print(s*(int(A[i][0]*50)*m))

prologue = tensor([H]*(n+1))
epilogue = tensor([I]*n+[H])
show_label = lambda x: print("="*25 + f"[ {x} ]" + "="*25)
show_label("start")
show(prologue @ s)
show_label("After Oracle")
show(O @ prologue @ s)
show_label("After 1 Grover")
show(G @ prologue @ s)
show_label("After 1 Grover & Oracle")
show(O @ G @ prologue @ s)
show_label("After 2 Grover")
show(G @ G @ prologue @ s)



out = epilogue @ G @ G @ prologue @ s
# print(np.round(out, 2))

