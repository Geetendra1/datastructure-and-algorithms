from collections import deque

def topologicalSort(adj, V):
    in_degree = [0] * V

    for u in range(V):
        for v in adj[u]:
            in_degree[v] += 1

    q = deque()

    for u in range(V):
        if in_degree[u] == 0:
            q.append(u) 
    
    while q:
        u = q.popleft()
        print(u, end=" ")

        for v in adj[u]:
            in_degree[v] -= 1 
            if in_degree[v] == 0 :
                q.append(v) 

 

def addEdge(adj, u, v):
    adj[u].append(v)

if __name__ == "__main__":
    V = 5
    adj = [[] for _ in range(V)]
    addEdge(adj, 0, 2)
    addEdge(adj, 0, 3)
    addEdge(adj, 1, 3)
    addEdge(adj, 1, 4)
    addEdge(adj, 2, 3)

    print("Following is a Topological Sort of")
    topologicalSort(adj, V)