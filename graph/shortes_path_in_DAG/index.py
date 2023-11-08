
def dfsr(adj, s, i, visited):
    visited[i] = True

    for v in adj[i]:
        print('v',v)
        if not visited[v]:
            dfsr(adj, s, v, visited)
    
    s.append(i)


def topologicalSort(adj,V):
    visited = [False] * V
    s = []

    for i in range(V):
        if not visited[i]:
            dfsr(adj, s, i, visited)
    
    return s

def shortestPath(adj, V,s):
    dist = [float("inf")] * V

    topologicalSortedA = topologicalSort(adj,V)

    print('topologicalSortedA',topologicalSortedA)
    



def addEdge(adj, u, v,w):
    adj[u].append((v, w))


if __name__ == "__main__":
    V = 6
    adj = [[] for _ in range(V)]
    addEdge(adj,0, 1, 5)
    addEdge(adj,0, 2, 3)
    addEdge(adj,1, 3, 6)
    addEdge(adj,1, 2, 2)
    addEdge(adj,2, 4, 4)
    addEdge(adj,2, 5, 2)
    addEdge(adj,2, 3, 7)
    addEdge(adj,3, 5, 1)
    addEdge(adj,3, 4, -1)
    addEdge(adj,4, 5, -2)

    print('adj', adj)
    print("Following is a Topological Sort of")
    s = 0
    shortestPath(adj, V, s)