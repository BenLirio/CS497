import numpy as np


def tensor(lst):
  hd, *tl = lst
  if not tl:
    return hd
  return np.kron(hd, tensor(tl))

n = 4
H = np.array([
    [1, 1],
    [1, -1]
]) / np.sqrt(2)
Hn = tensor([H]*n)

ket = lambda x: np.array([[1-x], [x]])
zero = lambda n: tensor([ket(0)]*n)
phase_shift = (2 * (zero(n) @ zero(n).T) - np.eye(2**n))

print(Hn @ phase_shift @ Hn)