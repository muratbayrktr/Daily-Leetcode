/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return NULL;

        queue<Node*> q; // Queue to manage the nodes to visit
        unordered_map<Node*, bool> visited; // Keep track of visited nodes
        unordered_map<Node*, Node*> clone;

        Node* cloneNode = new Node(node->val);

        q.push(node); // Start from the given node
        visited[node] = true; // Mark the start node as visited
        clone[node] = cloneNode;

        while (!q.empty()) {
            Node* current = q.front(); // Get the front node from the queue
            q.pop(); // Remove the front node

            // Process the current node (For demonstration, we'll just print its value)
            cout << current->val << " " << endl;

            // Visit all the neighbors of the current node
            for (Node* neighbor : current->neighbors) {
                // If this neighbor hasn't been visited yet
                if (!visited[neighbor]) {
                    q.push(neighbor); // Add it to the queue
                    visited[neighbor] = true; // Mark it as visited
                    clone[neighbor] = new Node(neighbor->val);
                    cout << "cloning " << neighbor->val << std::endl; 
                }
                clone[current]->neighbors.push_back(clone[neighbor]);
            }
        }
        return cloneNode;
    }
};