
from collections import deque

def BFS(adj, V, s, dist ):
    visited = [False] * V
    visited[s] = True
    q = deque()

    q.append(s)

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.append(v)


def main(): 
    V = 4
    adj = [[] for _ in range(V)]
    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 0, 2)
    addEdge(adj, 1, 3)

    dist = [float('inf')] * V
    dist[0] = 0
    BFS(adj, V, 0, dist)

    print('shorted path = ', dist)

def addEdge(adj,v,u):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    main()