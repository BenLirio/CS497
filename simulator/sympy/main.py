from sympy import init_printing, Symbol, Matrix, sqrt, simplify
from sympy.physics.quantum import TensorProduct
from functools import reduce
from math import log2

init_printing()

H = Matrix([
  [ 1,  1 ],
  [ 1, -1 ]
]) / sqrt(2)

Z = Matrix([
  [ 1, 0 ],
  [ 0, -1 ]
])
X = Matrix([
  [ 0, 1 ],
  [ 1, 0 ]
])

I = Matrix([
  [ 1, 0 ],
  [ 0, 1 ]
])

CNOT = Matrix([
  [ 1, 0, 0, 0 ],
  [ 0, 1, 0, 0 ],
  [ 0, 0, 0, 1 ],
  [ 0, 0, 1, 0 ]
])

m = [
  Symbol('m0'),
  Symbol('m1'),
]

def conditional_gate(gate, condition):
  identity = Matrix.eye(gate.shape[0])
  return (condition * gate) + ((1 - condition) * identity)

gates = [
  TensorProduct(H, I),
  CNOT,
  conditional_gate(TensorProduct(X, I), m[0]),
  conditional_gate(TensorProduct(Z, I), m[1]),
  CNOT,
  TensorProduct(H, I),
]

ket0 = Matrix([
  [ 1 ],
  [ 0 ],
])
initial_state = TensorProduct(ket0, ket0)

out = reduce(lambda s, g: g * s, gates, initial_state)
print(simplify(out))