/**
 * Implement shortest path in a DAG using the following algorithm in C++
 * 
 * 1. Initialize dist[v] = [INT_MAX, INT_MAX, ......]
 * 2. dist[s] = 0
 * 3. Find the topological sort of the graph
 * 4. For every vertex u in the topological sort
 * 5.     For every adjacent v of u
 * 6.         if dist[v] > dist[u] + weight(u,v)
 * 7.             dist[v] = dist[u] + weight(u,v)
 * 
 */

// Initialize dist[] with INT_MAX
int dist[V];
for(int i=0; i<V; i++){
    dist[i] = INT_MAX;
}

// Set the distance of the source vertex to 0
dist[s] = 0;

// Find the topological sort of the graph
vector<int> topologicalSort = topologicalSortDFS(adj, V);

// Traverse the vertices in the topological sort order
for(int u : topologicalSort){
    // Update the distances of the adjacent vertices
    for(int v : adj[u]){
        if(dist[v] > dist[u] + weight(u, v)){
            dist[v] = dist[u] + weight(u, v);
        }
    }
}

