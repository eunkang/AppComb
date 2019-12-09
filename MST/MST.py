from Graph import Graph


class Node:
    def __init__ (self, label):
        self.label = label
    def __str__(self):
        return self.label


def makeSet(x):
     x.parent = x
     x.rank   = 0


def union(x, y):
     xRoot = find(x)
     yRoot = find(y)
     if xRoot.rank > yRoot.rank:
         yRoot.parent = xRoot
     elif xRoot.rank < yRoot.rank:
         xRoot.parent = yRoot
     elif xRoot != yRoot:
         yRoot.parent = xRoot
         xRoot.rank = xRoot.rank + 1


def find(x):
     if x.parent == x:
        return x
     else:
        x.parent = find(x.parent)
        return x.parent


def kruskal(G):

    #minimum spanning tree

    result = tuple()
    ans = set()
    i = 0
    e = 0

    V = G.V
    N = {v:Node(v) for v in G.V}
    for v in G.V:
        makeSet(N[v])

    while e < len(V) - 1:

        G.E = sorted(list(G.E), key=lambda x:x[-1])
        u,v,w = G.E[i]
        i += 1
        x = find(N[u])
        y = find(N[v])

        if x != y :
            e += 1
            result = (u,v,w)
            union(x, y)

        ans.add(result)

    return Graph(V,ans)


def transform(G):

    #maximum spanning tree


    # result = tuple()
    # ans = set()
    # i = 0
    # e = 0
    #
    # V = G.V
    # N = {v: Node(v) for v in G.V}
    # for v in G.V:
    #     makeSet(N[v])
    #
    # while e < len(V) - 1:
    #
    #     E = sorted(list(G.E), key=lambda x: x[-1])
    #     E = E[::-1]
    #     u, v, w = E[i]
    #     i += 1
    #     x = find(N[u])
    #     y = find(N[v])
    #
    #     if x != y:
    #         e += 1
    #         result = (u, v, -w)
    #         union(x, y)
    #
    #     ans.add(result)

    i = 0
    e = 0

    result = tuple()
    ans = set()

    while e < len(G.V) - 1:
        E = sorted(list(G.E), key=lambda x: x[-1])
        E = E[::-1]
        u, v, w = E[i]
        i += 1

        if w > 0:
            result = (u, v, -w)

        ans.add(result)



    return Graph(G.V,ans)

#
# g_1 = Graph({1, 2, 3}, {(1, 2, 2), (2, 3, 3), (1, 3, 1)})
# print(kruskal(g_1))
# print(kruskal(transform(g_1)))