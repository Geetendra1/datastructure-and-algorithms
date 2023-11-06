#include <iostream>
#include <queue>
using namespace std;
#define V 4

int primMST(int graph[V][V]) {
    // Create a set mstSet that keeps track of vertices already included in MST.
    bool mSet[V];
    int res = 0; 
    // Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE
    int key[V];
    fill(key, key+V, INT_MAX);

    // Assign key value as 0 for the first vertex so that it is picked first.
    // key[] = [0, INF, INF, INF]
    key[0] = 0; 
    
// While mstSet doesn't include all vertices:
	for (int count = 0; count < V ; count++) {
    int u = -1; 
        // Pick a vertex u which is not there in mstSet and has minimum key value.
        for(int i = 0; i< V; i ++){
            if(!mSet[i] && ( u==-1 || key[i]<key[u])){
                u=i;
            }
        }
        // Include u to mstSet.
        mSet[u] = true; 
		res+=key[u];
    
// Update key value of all adjacent vertices of u
// To update the key values, iterate through all adjacent vertices. 
    for (int v = 0; v < V; v++) {
        // For every adjacent vertex v, 
        // if weight of edge u-v is less than the previous key value of v, update the key value as weight of u-v.
        if (graph[u][v]!=0 && mSet[v] == false) {
            key[v] = min(key[v],graph[u][v]); 
        }
    }
}
return res;
}

int main() 
{ 
	int graph[V][V] = { { 0, 5, 8, 0}, 
						{ 5, 0, 10, 15 }, 
						{ 8, 10, 0, 20 }, 
						{ 0, 15, 20, 0 },}; 

	cout<<primMST(graph); 

	return 0; 
} 