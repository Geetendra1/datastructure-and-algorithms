from collections import deque


def BFS(adj, V, s):
    visited = [False] * V
    q = deque() 

    visited[s] = True
    q.append(s)

    while q:
        u = q.popleft()
        print(u, end=" ")

        
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)



def main(): 
    V = 5
    adj = [[] for _ in range(V)]
    s = 0
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 1, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 2, 4)

    BFS(adj,V,s)

def addEdge(adj,v,u):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    main()