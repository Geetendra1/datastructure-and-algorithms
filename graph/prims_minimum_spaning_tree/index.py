
def prims(graph,V):
    key = [float('inf')] * V
    res = 0
    mSet = [False] * V
    key[0] = 0

    for count in range(V):
        u = -1

        for i in range(V):
            if not mSet[i] and (u == -1 or key[i] < key[u]):
                u = i   
        mSet[u] = True
        res += key[u]

        for v in range(V):
            if graph[u][v] != 0 and not mSet[v]:
                key[v] = min(key[v], graph[u][v])

    return res




if __name__ == "__main__":
    V = 4
    graph = [[0, 5, 8, 0],
            [5, 0, 10, 15],
            [8, 10, 0, 20],
            [0, 15, 20, 0]]
    
    # prims(graph, V)
    print(prims(graph, V))