
import sys


def prims(graph,V, src):
    key = [sys.maxsize] * V
    mSet = [False] * V
    key[src] = 0

    for count in range(V-1):
        u = -1

        for i in range(V):
            if not mSet[i] and (u == -1 or key[i] < key[u]):
                u = i   
        mSet[u] = True

        for v in range(V):
            if graph[u][v] != 0 and not mSet[v]:
                key[v] = min(key[v], key[u] + graph[u][v])

    return key




if __name__ == "__main__":
    V = 4
    graph = [[0, 50, 100, 0],
            [50, 0, 30, 200 ],
            [100, 30, 0, 20 ],
            [0, 200, 20, 0]]
    
    # prims(graph, V)
    print(prims(graph, V , 0))