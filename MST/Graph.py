class Graph:
  def __init__(self,V,E):
    self.V = V
    self.E = E
  def __eq__(self, other):
    return self.V == other.V and self.E == other.E
