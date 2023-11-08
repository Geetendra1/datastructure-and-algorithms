def DFSR(adj, s, visited, temp):
    visited[s] = True
    temp[s] = True

    for v in adj[s]:
        if not visited[v]:
            if DFSR(adj, v, visited, temp):
                return True
        elif temp[v] :
            return True
    
    temp[s] = False
    return False

def DFS(adj, V):
    visited = [False] * V
    temp = [False] * V

    for i in range(V):
        if not visited[i]:
            if DFSR(adj, i, visited, temp):
                return True
    return False



def main():
    V = 6
    adj = [[] for _ in range(V)]
    addEdge(adj, 0, 1)
    addEdge(adj, 2, 1)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 4, 5)
    addEdge(adj, 5, 3)

    if DFS(adj, V):
        print("Cycle found")
    else:
        print("No cycle found")


def addEdge(adj,v,u):
    adj[u].append(v)

if __name__ == "__main__":
    main()