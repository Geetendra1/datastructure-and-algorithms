
def dfsr(adj,s,visited,parent):
    visited[s] = True

    for u in adj[s]:
        if not visited[u]:
            if dfsr(adj, u , visited, s):
                return True
        elif u!= parent:
            return True
    return False

def dfs(adj, V):
    visited = [False]* V

    for v in range(V):
        if not visited[v]:
            if dfsr(adj, v, visited, -1):
                return True
            
    return False


def main():
    V = 6
    adj = [[] for _ in range(V)]

    addEdge(adj, 0, 1)


    if dfs(adj, V):
        print("Cycle found")
    else:
        print("No cycle found")



def addEdge(adj,v,u):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    main()