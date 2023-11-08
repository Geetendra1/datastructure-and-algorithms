def DFSR(adj, visited, s):
    visited[s] = True
    print(s, end=" ")

    for v in adj[s]:
        if not visited[v]:
            DFSR(adj, visited,v)

def DFS(adj,V, s):
    visited = [False] * V
    DFSR(adj, visited, s)


def main(): 
    V = 5
    adj = [[] for _ in range(V)]

    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 1, 3)
    addEdge(adj, 1, 4)
    addEdge(adj, 3, 4)

    print("Following is Depth First Traversal:")
    DFS(adj, V, 0)

def addEdge(adj,v,u):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    main()