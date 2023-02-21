from functools import reduce
import numpy as np

qbit = lambda x: np.array([float(x==0), float(x==1)])
H = lambda: np.array([[1, 1], [1, -1]]) / np.sqrt(2)
X = lambda: np.array([[0, 1], [1, 0]])
Z = lambda: np.array([[1, 0], [0, -1]])
CNOT = lambda: np.array([
  [1, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 1],
  [0, 0, 1, 0]
])
I = lambda: np.array([[1, 0], [0, 1]])
tensor = lambda *vs: reduce(np.kron, vs)

message = [1, 0]
state_str = lambda s: f'| {" | ".join(list(map(lambda x: "%.2f" % x, s)))} |'


s = tensor(qbit(0), qbit(0))
print(f"Initial state\n{state_str(s)}\n")
s = tensor(H(), I()) @ s
print(f"Alice applies H\n{state_str(s)}\n")
s = CNOT() @ s
print(f"Alice applies CNOT\n{state_str(s)}\n")

if message[0] == 1:
  s = tensor(X(), I()) @ s
  print(f"Alice encodes 1?\n{state_str(s)}\n")
if message[1] == 1:
  s = tensor(Z(), I()) @ s
  print(f"Alice encodes ?1\n{state_str(s)}\n")

s = CNOT() @ s
print(f"Bob applies CNOT\n{state_str(s)}\n")
s = tensor(H(), I()) @ s
print(f"Bob applies H\n{state_str(s)}\n")

for i in range(2):
  for j in range(2):
    if abs(s[i*2+j] - 1.0) < 1e-6:
      print(f"Bob measures {j}{i}")