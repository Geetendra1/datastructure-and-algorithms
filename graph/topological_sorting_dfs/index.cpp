#include <iostream>
#include <queue>
using namespace std;





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


void DFS(vector<int> adj[], int u,stack<int> &st, bool visited[]) 
{ 	
    visited[u]=true;
    
    for(int v:adj[u]){
        if(visited[v]==false)
            DFS(adj,v,st,visited);
    }
    st.push(u);
}

void topologicalSort(vector<int> adj[], int V){
    bool visited[V];

    for(int u=0; u<V; u++){
        visited[u] = false
    }

    stack<int> st;

    for(int u=0;u<V;u++){
        if(visited[u]==false){
            DFS(adj,u,st,visited);
        }
    }

    while(st.empty()==false){
        int u=st.top();
        st.pop();
        cout<<u<<" ";
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
    addEdge(adj,1, 3); 
    addEdge(adj,2, 3); 
    addEdge(adj,3, 4); 
    addEdge(adj,2, 4);  
  
    cout << "Following is a Topological Sort of\n"; 
    topologicalSort(adj,V);

	return 0; 
} 
