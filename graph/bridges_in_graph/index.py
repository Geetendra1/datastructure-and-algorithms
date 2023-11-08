from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u, visited, disc, low, parent):
        """
        This function is a utility function to find the bridges in the graph.
        It performs a Depth-First Search traversal of the graph and keeps track of discovery time and low values of the vertices.
        It also keeps track of parent vertices to avoid considering the same edge twice.
        """
        visited[u] = True  # Mark the current node as visited
        disc[u] = self.time  # Discovery time of a vertex
        low[u] = self.time  # Low value of a vertex
        self.time += 1  # Increment the time

        # Go through all vertices adjacent to this
        for v in self.graph[u]:
            if not visited[v]:  # If v is not visited yet, then make it a child of u in DFS tree and recur for it
                parent[v] = u
                self.bridge_util(v, visited, disc, low, parent)

                # Check if the subtree rooted with v has a connection to one of the ancestors of u
                # Update the low value of u to be the minimum of the current low value of u and the low value of v
                # This is done to keep track of the lowest reachable vertex from the subtree rooted at u
                low[u] = min(low[u], low[v])

                # If the lowest vertex reachable from subtree under v is below u in DFS tree, then u-v is a bridge
                if low[v] > disc[u]:
                    print(f"{u} - {v}")
            # If the adjacent vertex v is not the parent of u in the DFS tree, then update the low value of u
            # This is done to ensure that the low value of u is the minimum discovery time of all vertices reachable from u
            elif v != parent[u]:  
                low[u] = min(low[u], disc[v])

    def find_bridges(self):
        visited = [False] * self.V
        disc = [float("inf")] * self.V
        low = [float("inf")] * self.V
        parent = [-1] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.bridge_util(i, visited, disc, low, parent)

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print("Bridges in the graph:")
    g.find_bridges()
