# Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# class Node {
#      public int val;
#      public List<Node> neighbors;
#    }
 
# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). 
# For example, the first node with val == 1, the second node with val == 2, and so on. 
# The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph. 
# Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. 
# You must return the copy of the given node as a reference to the cloned graph.

# We are given a node from connected undirected graph. Each node consists of a value and a list of neighbours.
# Our goal is to create a deep copy of the entire graph and return the cloned version of the starting node. 
# A deep copy is basically creating new nodes. Graphs can have cycles, but we need to avoid cloning the same node.
# We can use a hashmap or a dictionary which will map { original_node --> cloned_node}. We can then use depth first search. 
# If a node already has clones, we will reuse it instead of creating a new one.

# Why DFS?
# Graph is an interconnected network with potential cycles and deep branch structures, and DFS provides
# a systematic way to discover, instantiate and wire up every node without getting stuck in infinite loops.
# DFS can say we pick a starting node, plunge deep down its neighbor connections until we hit a node we have already cloned,
# and then backtrack to handle the remaining neighbours

# Deep Copies will require Creation and Connection
# Every graph node has its value (node.value) and Connections (node.neighbours)

# When we are standing at Node A, I can create clone A. DFS says - " I will create Clone A first, but before I finish Clone A, let me recursively"
# run DFS on its neighbours so I can get their cloned references and append them into Clone A.neighbours.

# Cycle Prevention with the HashMap
# Graphs can contain cycle so a recursion won't work. 
# When we pair DFS with a Hash Map, the search serves as a safety guard. 
# Before exploring a neighbours, we check if it is in clones.
# If neighbours is already in clones, we create clone[neighbor] and recursively run DFS on it

# Depth First Search
# 1. Explores as deep as possible along each branch before backtracking.
# 2. Recursive (or using a Explicit Stack)

# Breadth First Search
# 1. Explores level by level using a Queue
# 2. Iterative using a Queue

from typing import Optional

# 1. Define the Node Class
class Node:
    def __init__(self, val: int = 0, neighbors: list['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self,node: Optional['Node']) -> Optional['Node']:
        # Edge Case : If the graph is empty, we will return None
        if not node:
            return None
    
        # Create a Hashmap or Dictionary to keep track of cloned nodes
        # Key : Original Node and Value : Cloned Node
        # This map does two things :
        # 1. Memoization : It caches created copies so we don't recreate a node we already clone
        # 2. Cycle Safety : If a cycle is detected, we stop an infinite recursion loop
        visited = {}
    
        # Let's create a definition of Depth First Search (DFS)
        def dfs(curr):
            # If this node is already cloned and exists in Dict/Hashmap, we stop exploring and then we return the existing clone
            if curr in visited:
                return visited[curr]
        
            # Create a clone of the current node
            # We create a new Node instance with the same scalar value (curr.val) but an empty .neighbors list.
            # We put it into visited before processing its neighbors so downstream recursive calls can find it.
            clone = Node(curr.val)
        
            # Storing the node in the visited map
            visited[curr] = clone
        
            # Clone all the neighbours (Recursion)
            # For each neighbour, dfs(neighbor), we return its cloned counterpart, which we append to the neighbors
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))
        
            return clone

        # Start DFS from the given node
        return dfs(node)

# To test :
# 1. Define the Node Class
# 2. Instantiate Individual nodes and populate their neighbor lists to form the graph
# 3. Pass the root node to cloneGraph()

from typing import Optional, List


# --- 2. Constructing a Test Graph ---
# Let's create a 4-node square graph:
# 1 <---> 2
# ^       ^
# |       |
# v       v
# 4 <---> 3

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Wire up the undirected edges
node1.neighbors = [node2,node4]
node2.neighbors = [node1,node3]
node3.neighbors = [node2,node4]
node4.neighbors = [node1,node3]

sol = Solution()
cloned_node1 = sol.cloneGraph(node1)

# --- 4. Verify Deep Copy ---
print("Original Node 1 Memory Address:", hex(id(node1)))
print("Cloned Node 1 Memory Address:  ", hex(id(cloned_node1)))
print("Are they separate objects?", node1 is not cloned_node1) # True
print("Do they share the same value?", node1.val == cloned_node1.val) # True
print("Cloned Node 1 Neighbors' Values:", [n.val for n in cloned_node1.neighbors]) # [2, 4]


