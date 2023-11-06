#include <iostream>
#include <queue>
using namespace std;using namespace std;

/**
 * LOGIC - every visited[i] == false is the source
 * 
 * 
 * BFSA - create a boolean array visited[] of size V.
 * BFSA - loop through this visted array and assign each item to False.
 * BFSA - loop through this visted array and check every visted[i] == fasle.
 * BFSA - for every visited[i] == false call BFS() function.
 * BFS -  create a queue<int> q.
 * BFS -  make visited[s] = true;
 * BFS - push 's' which is source into this queue.
 * BFS - Run a while loop of conditon queue.empty() == false.
 * BFS - in loop(while) - get the first item out of the queue and assign to to var 'u'.
 * BFS - in loop(while) - in loop(for) - run another 'for' loop for all the adjecent of 'u'.
 * BFS -in loop(while) - in loop(for) - check if the the visited[u] == false.
 * BFS -in loop(while) - in loop(for) - mark visited[u] == true , push the 'u' inside the queue. 
*/


void BFS(vector<int> adj[], int s, bool visited[]) 
{ 	queue<int>  q;
	
	visited[s] = true; 
	q.push(s); 

	while(q.empty()==false) 
	{ 
		int u = q.front(); 
		q.pop();
		cout << u << " "; 
		 
		for(int v:adj[u]){
		    if(visited[v]==false){
		        visited[v]=true;
		        q.push(v);
		    }
		} 
	} 
}

void BFSA(vector<int> adj[], int V){
    bool visited[V]; 
	for(int i = 0;i<V; i++) 
		visited[i] = false;
		
    for(int i=0;i<V;i++){
        if(visited[i]==false)
            BFS(adj,i,visited);
    }
}

void addEdge(vector<int> adj[], int u, int v){
    adj[u].push_back(v);
    adj[v].push_back(u);
}

int main() {
    int V = 7;
    vector<int> adj[V];
    
	addEdge(adj,0,1); 
	addEdge(adj,0,2); 
	addEdge(adj,2,3); 
	addEdge(adj,1,3); 
	addEdge(adj,4,5);
	addEdge(adj,5,6);
	addEdge(adj,4,6);
	BFSA(adj,V);
	return 0;
}