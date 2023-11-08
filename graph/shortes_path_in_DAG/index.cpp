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


/**
 * topologicalSort - create a bool arrray of lenth V.
 * topologicalSort - make all elemets inside this array to false 
 * topologicalSort - create a stack <int> st.
 * topologicalSort - for every value wehere visited[i] = false  call  DFS(adj,u,st,visited);
 * 
 * DSF - make visted[s] = true; 
 * DSF - run a for loop for all adjecent of u. 
 * DSF - for every visited[v] = false , make resursive call for DFS(adj,u,st,visited);
 * DSF - if not adject any more - push u to stack
 * 
 * topologicalSort - is stack is not empty print every element from that stack
*/

#include <iostream>
#include <vector>
#include <stack>
#include <climits>

using namespace std;

const int V = 6; // Define the number of vertices

// Function to perform a topological sort using DFS
void topologicalSortDFS(vector<vector<int>>& adj, int v, vector<bool>& visited, stack<int>& stack) {
    visited[v] = true;
    for (int u : adj[v]) {
        if (!visited[u]) {
            topologicalSortDFS(adj, u, visited, stack);
        }
    }
    stack.push(v);
}

// Function to find the topological sort of the graph
vector<int> topologicalSort(vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    stack<int> stack;
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            topologicalSortDFS(adj, i, visited, stack);
        }
    }
    vector<int> result;
    while (!stack.empty()) {
        result.push_back(stack.top());
        stack.pop();
    }
    return result;
}

// Function to find the shortest path in a DAG
void shortestPathDAG(vector<vector<int>>& adj, int s) {
    int dist[V];
    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
    }

    dist[s] = 0;

    vector<int> topologicalSortOrder = topologicalSort(adj, V);

    for (int u : topologicalSortOrder) {
        for (int v : adj[u]) {
            if (dist[v] > dist[u] + 1) { // Change '1' to the actual weight function weight(u, v)
                dist[v] = dist[u] + 1; // Change '1' to the actual weight function weight(u, v)
            }
        }
    }

    // Print the shortest distances from the source vertex
    for (int i = 0; i < V; i++) {
        cout << "Shortest distance from vertex " << s << " to vertex " << i << " is: " << dist[i] << endl;
    }
}

int main() {
    vector<vector<int>> adj(V);

    // Define the DAG's edges and weights
    // Example graph:
    // (0) -> (1) -> (2)
    //  |            |
    //  v            v
    // (3) -> (4) -> (5)

    adj[0].push_back(1);
    adj[3].push_back(1);
    adj[1].push_back(2);
    adj[4].push_back(2);
    adj[4].push_back(5);

    int sourceVertex = 0; // Define the source vertex

    shortestPathDAG(adj, sourceVertex);

    return 0;
}



