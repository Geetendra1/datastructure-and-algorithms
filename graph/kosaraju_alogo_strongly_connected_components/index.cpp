#include <iostream> 
#include <list> 
#include <stack> 
using namespace std; 

// Class representing a directed graph
class Graph 
{ 
	int V; // Number of vertices
	list<int> *adj; // Pointer to an array containing adjacency lists
	
	// Recursive function to fill the stack with vertices in DFS order
	void fillOrder(int v, bool visited[], stack<int> &s); 
 
	// Recursive function to perform DFS traversal starting from a given vertex
	void DFSUtil(int v, bool visited[]); 
public: 
	// Constructor
	Graph(int V); 
	
	// Function to add an edge to the graph
	void addEdge(int v, int w); 
	 
	// Function to print strongly connected components
	void printSCCs(); 

	// Function to get the transpose of the graph
	Graph getTranspose(); 
}; 

// Constructor
Graph::Graph(int V) 
{ 
	this->V = V; 
	adj = new list<int>[V]; 
} 

// Recursive function to perform DFS traversal starting from a given vertex
void Graph::DFSUtil(int v, bool visited[]) 
{ 
	// Mark the current node as visited and print it
	visited[v] = true; 
	cout << v << " "; 

	// Recur for all the vertices adjacent to this vertex
	list<int>::iterator i; 
	for (i = adj[v].begin(); i != adj[v].end(); ++i) 
		if (!visited[*i]) 
			DFSUtil(*i, visited); 
} 

// Function to get the transpose of the graph
Graph Graph::getTranspose() 
{ 
	Graph g(V); 
	for (int v = 0; v < V; v++) 
	{ 
		list<int>::iterator i; 
		for(i = adj[v].begin(); i != adj[v].end(); ++i) 
		{ 
			g.adj[*i].push_back(v); 
		} 
	} 
	return g; 
} 

// Function to add an edge to the graph
void Graph::addEdge(int v, int w) 
{ 
	adj[v].push_back(w); 
} 

// Recursive function to fill the stack with vertices in DFS order
void Graph::fillOrder(int v, bool visited[], stack<int> &s) 
{ 
	// Mark the current node as visited
	visited[v] = true; 

	// Recur for all the vertices adjacent to this vertex
	list<int>::iterator i; 
	for(i = adj[v].begin(); i != adj[v].end(); ++i) 
		if(!visited[*i]) 
			fillOrder(*i, visited, s); 
 
	// Push the current vertex to the stack
	s.push(v); 
} 

// Function to print strongly connected components
void Graph::printSCCs() 
{ 
	stack<int> s; // Stack to store the vertices in DFS order
 
	bool *visited = new bool[V]; // Array to track visited vertices
	for(int i = 0; i < V; i++) 
		visited[i] = false; 
 
	// Fill the stack with vertices in DFS order
	for(int i = 0; i < V; i++) 
		if(visited[i] == false) 
			fillOrder(i, visited, s); 

	// Get the transpose of the graph
	Graph gr = getTranspose(); 

	// Reset the visited array
	for(int i = 0; i < V; i++) 
		visited[i] = false; 

	// Process the vertices in the stack
	while (s.empty() == false) 
	{ 
		int v = s.top(); 
		s.pop(); 
 
		// Print the strongly connected component if not visited
		if (visited[v] == false) 
		{ 
			gr.DFSUtil(v, visited); 
			cout << endl; 
		} 
	} 
} 

int main() 
{ 
	Graph g(5); // Create a graph with 5 vertices
	g.addEdge(1, 0); // Add edges to the graph
	g.addEdge(0, 2); 
	g.addEdge(2, 1); 
	g.addEdge(0, 3); 
	g.addEdge(3, 4); 

	cout << "Following are strongly connected components in the given graph: \n"; 
	g.printSCCs(); // Print the strongly connected components

	return 0; 
}
