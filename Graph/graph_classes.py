class Graph1:
  def __init__(self, n, E):
    self.n = n
    self.E = E
  def __eq__(self, other):
    return (type(self) == type(other) and self.n == other.n and self.E == other.E)

class Graph2:
  def __init__(self, A):
    self.A = A
  def __eq__(self, other):
    return (type(self) == type(other) and self.A == other.A)

class Graph3:
  def __init__(self, M):
    self.M = M
  def __eq__(self, other):
    return (type(self) == type(other) and self.M == other.M)
