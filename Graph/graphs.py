from graph_classes import Graph1, Graph2, Graph3

def G1ToG2(G):

  final_list = []
  edge_list = sorted(G.E)
  n_vertex = G.n
  empty_set = set()

  new_dict = dict((y,x) for x,y in G.E)

  for i in range(n_vertex):
    if i not in new_dict:
      final_list.append(set())
    else:
      for j in edge_list:
        if i == j[0]:
          new_other1 = j[1]
          empty_set.add(new_other1)
      final_list.append(empty_set)
      empty_set = set()
  return Graph2(final_list)


def G2ToG3(G):

  dict = {}
  n = len(G.A)

  for x in range(0, n):
    dict[x] = G.A[x]

  # Matrix
  M = [[0] * n for i in range(n)]

  keys = sorted(dict.keys())

  for a,b in [(keys.index(a), keys.index(b)) for a, row in dict.items() for b in row]:
    M[a][b] = 1

  return Graph3(M)

def G3ToG1(G):
  return G2ToG1(G3ToG2(G))

def G1ToG3(G):
  return G2ToG3(G1ToG2(G))

def G2ToG1(G):

  n = len(G.A)
  final = set()

  for i in range(n):
    for j in range(len(G.A[i])):
      tup = (i, list(G.A[i])[j])
      final.add(tup)
  return Graph1(n, final)

def G3ToG2(G):

  dict = {}
  new_list = []

  for i in range(0, len(G.M)):
    for j in range(0, len(G.M)):
      if G.M[i][j]:
        dict.setdefault(i,set())
        dict[i].add(j)
    if dict.get(i) != None:
      new_list.append(dict.get(i))
    if dict.get(i) is None:
      new_list.append(set())
  return Graph2(new_list)


# Let G be the graph depicted on the assignment sheet
# Below are three different representations of G

G1 = Graph1(4, {(2,2),(0,2),(0,1), (1,0)})
G2 = Graph2([{1,2},
            {0},
            {2},
            set()])
G3 = Graph3([[0,1,1,0],
            [1,0,0,0],
            [0,0,1,0],
            [0,0,0,0]])
#If your implementation of the functions above are correct, each of the following should return as True
# print(G1ToG2(G1) == G2) #yes
# print(G2ToG3(G2) == G3) #yes
# print(G3ToG1(G3) == G1)
# print(G1ToG3(G1) == G3) #yes
# print(G2ToG1(G2) == G1)
# print(G3ToG2(G3) == G2) #yes

