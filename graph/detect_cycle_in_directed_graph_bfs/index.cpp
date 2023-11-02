#include <iostream>
#include <queue>
using namespace std;


void topologicalSort(vector<int> adj[], int V){
    vector<int> in_degree(V,0);

    for (int u = 0; u < V; u++) { 
        for (int x:adj[u]) 
            in_degree[x]++; 
    } 

    queue<int> q;

    for (int u = 0; u < V; u++) { 
        if(in_degree[u] == 0){
            q.push(u);
        }
    } 
    int count=0;  

    while(q.empty() == false){
        int u = q.front();
        q.pop();
        count++;
        for(int x:adj[u]){
            if(--in_degree[x] == 0){
                q.push(x);
            }
        }
    }

    if (count != V) { 
        cout << "There exists a cycle in the graph\n"; 
    }
    else{
        cout << "There exists no cycle in the graph\n";
    }

}


void addEdge(vector<int> adj[], int u, int v){
    adj[u].push_back(v);
}

int main() 
{ 
	int V=5;
	vector<int> adj[V];
	addEdge(adj,0, 1); 
    addEdge(adj,4, 1); 
    addEdge(adj,1, 2); 
    addEdge(adj,2, 3); 
    addEdge(adj,3, 1);  
  
    topologicalSort(adj,V);

	return 0; 
} 