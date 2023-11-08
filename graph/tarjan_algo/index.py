#code
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
    
    def add_edge(self, v, w):
        self.adj[v].append(w)
    
    def SCCUtil(self, u, disc, low, st, stackMember):
        global time
        time += 1
        disc[u] = time
        low[u] = time
        st.append(u)
        stackMember[u] = True
        print('u',u)
        print('lowest', low)
        for v in self.adj[u]:
            print('v',v)
            
            if disc[v] == -1:
                self.SCCUtil(v, disc, low, st, stackMember)
                low[u] = min(low[u], low[v])
                print('low-1', low , 'u->', u , 'v->', v )
            elif stackMember[v]:
                print('stackMember-v', v)
                print('stackMember-u',u)
                low[u] = min(low[u], disc[v])
                print('low-2',  low , 'u->', u , 'v->', v)
        
        w = 0
        if low[u] == disc[u]:
            while st[-1] != u:
                w = st[-1]
                print(w, end=" ")
                stackMember[w] = False
                st.pop()
            w = st[-1]
            print(w)
            stackMember[w] = False
            st.pop()
    
    def SCC(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stackMember = [False] * self.V
        st = []

        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, disc, low, st, stackMember)

time = 0

if __name__ == "__main__":
    print("SCCs in the graph")
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    g.SCC()
