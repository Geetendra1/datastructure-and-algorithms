from collections import defaultdict

def dfsr(adj, s, i, visited):
    visited[i] = True

    for v in adj[i]:
        if not visited[v]:
            dfsr(adj, s, v, visited)
    
    s.append(i)


def topologicalSort(adj,V):
    visited = [False] * V
    s = []

    for i in range(V):
        if not visited[i]:
            dfsr(adj, s, i, visited)

    while s:
        u = s.pop()
        print(u, end=" ")



def addEdge(adj, u, v):
    adj[u].append(v)

if __name__ == "__main__":
    V = 5
    adj = defaultdict(list)
    addEdge(adj, 0, 1)
    addEdge(adj, 1, 3)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 2, 4)
    
    print("Following is a Topological Sort of")
    topologicalSort(adj, V)