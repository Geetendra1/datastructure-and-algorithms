#include <iostream>
#include <queue>
using namespace std;


/**
 * create a boolean array visited[] of size V.
 * loop through this visted array and assign each item to False.
 * create a queue<int> q.
 * make visited[s] = true;
 * push 's' which is source into this queue.
 * Run a while loop of conditon queue.empty() == false.
 * in loop - get the first item out of the queue and assign to to var 'u'.
 * in loop - run another loop for all the adjecent of 'u'.
 * in loop - in loop - check if the the visited[u] == false , push the 'u' inside the queue. 
*/

void BFS(vector<int> adj[], int V, int s) {
    bool visited[V];
    for(int i=0; i<V; i++){
        visited[i] = false;
    }
    
    queue<int> q;
    visited[s] = true; 
    q.push(s);
    
    while(q.empty() == false){
        int u = q.front();
        q.pop();
        cout << u << " ";
        
        for(int v:adj[u]){
            if(visited[v] == false){
                visited[v] = true;
                q.push(v);
            }
        }
    }
}

void addEdge(vector<int> adj[], int u, int v){
    adj[u].push_back(v);
    adj[v].push_back(u);
}

int main() {
    int V = 5;
    vector<int> adj[V];
    
    addEdge(adj,0,1); 
	addEdge(adj,0,2); 
	addEdge(adj,1,2); 
	addEdge(adj,2,3); 
	addEdge(adj,1,3);
	addEdge(adj,3,4);
	addEdge(adj,2,4);
	
	BFS(adj,V,0); 

	
    return 0;
}