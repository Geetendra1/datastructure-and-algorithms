from collections import deque

def BFS(adj, visited, s):
    visited[s] = True
    q = deque()
    q.append(s)

    while q:
        u = q.popleft()
        print(u, end=" ")

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)


def BFSA(adj, V):
    visited = [False] * V
    count = 0
    for i in range(V):
        if not visited[i]:
            BFS(adj, visited, i)
            count += 1
    return count


def main(): 
    V = 7
    adj = [[] for _ in range(V)]
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 1, 3)
    addEdge(adj, 4, 5)
    addEdge(adj, 5, 6)
    addEdge(adj, 4, 6)

    print("Number of islands:", BFSA(adj, V))

def addEdge(adj,v,u):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    main()