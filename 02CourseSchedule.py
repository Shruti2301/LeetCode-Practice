# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# We are given numCourses (total number of courses labeled from 0 to numCourses - 1)
# Prerequisite --> a list of pairs [a,b] : to take course a, one needs to finish b first
# Our goal is to determine if it is possible to finish all courses given prerequisites
# Return True if we can complete all the courses, otherwise we return False. Need to check cycles!
# Each course == A node and Each prerequisite = [a,b] = a directed edge in a graph ( b ---> a


# We can build the graph using adjacency list
# graph[b] will contain all the courses that depend on b 
# This line creates an empty dictionary with default values, new or missing key starts with empty list []

# We can 3 main data structures :
#
# Adjacency List (Graph) : By using dict or defaultdict(list) - The input will give use prerequisites as edge pairs like [a,b]
# meaning to take course a, we need to take course b first. We convert this to a directed graph where each course points to its dependent course (b --> a)
#
# In Degree Array/ Map for BFS 
# Use List/Array or Dictionary of Integers ( indegree = [0] * numCourses) - we need to track how many prerequisites each course requires

# Queue (for BFS) or Recursion Stack (for DFS)
# collections.deque to keep track of all courses that currently have 0 prerequisites remaining. We can pop a course from the front, "take" it and check if it unlocks any new course
# Depth First Search : to track visited state list/set
# 0 = Unvisited , 1 = Visiting (currently in active recursion call stack), 2 = Visited (fully processesed already)
# If our DFS hits a node in state 1 ('Visiting') --> we found a cycle, it is impossible to finish all the courses.
#


from collections import defaultdict

# Ex : graph['A'].append('B) 
# Python sees that 'A' does not exist in graph yet.
# It calls list() automatically create a new empty list [] for 'A' and appends 'B' to that list

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    
    # Build the graph using adjacency list
    # graph[b] will contain all the courses that depend on b
    graph = defaultdict(list)
    
    # Ex : graph['A'].append('B')
    # Python sees that 'A' does not exist in the graph yet.
    # It calls list() to automatically create a new empty list [] for 'A' and appends 'B' to that list
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # Create an array to track visited node and DFS path
    visited = [False] * numCourses  # Track Processed Nodes already
    path = [False] * numCourses # Mark nodes in recursion stack
    
    # Let me create a definition function for DFS with Backtracking
    # Cycle : Course A requires Course B, Course B requires Course C and Course C requires A --> return False)
    def dfs(course:int) -> bool:
        # If the course is already in the current path ==> cycle exists
        if path[course]:
            return False
        
        # If there is no cycle, skip because I have already checked this course and its prerequisites so its safe
        if visited[course]:
            return True
        
        # Mark course as visited and part of the current path : we have already evaluated it
        visited[course] = True
        path[course] = True
        
        # Loop through all the courses that depend on the current course
        for next_course in graph[course]:
            if not dfs(next_course):
                return False
        
        # Remove course from the current path after DFS
        # Now that I have checked all the dependent neighbors and found no cycles, we unmark it to false 
        # We are backtracking up the call stack to explore a different branch. This course is no longer part of the active search path.
        path[course] = False
        return True
    
    
    # Run DFS
    # Using a loop because this graph might be disconnected. We must trigger DFS for every single course from 0 to numCourses - 1
    for course in range(numCourses):
        if not dfs(course):
            return False
    
    # If no cycle detected, all courses can be finished
    return True

# Test Case 1: No cycle (1 -> 0)
# 2 courses: To take course 0, you must first take course 1.
numCourses1 = 2
prerequisites1 = [[0, 1]]
print("Test Case 1 Result:", canFinish(numCourses1, prerequisites1))
# Output: True


# Test Case 2: Direct Cycle (0 -> 1 -> 0)
# 2 courses: To take 0 you need 1, but to take 1 you need 0. Impossible!
numCourses2 = 2
prerequisites2 = [[0, 1], [1, 0]]
print("Test Case 2 Result:", canFinish(numCourses2, prerequisites2))
# Output: False


# Test Case 3: Longer Cycle (0 -> 1 -> 2 -> 0)
numCourses3 = 3
prerequisites3 = [[1, 0], [2, 1], [0, 2]]
print("Test Case 3 Result:", canFinish(numCourses3, prerequisites3))
# Output: False
     
# V (Vertices) = numCourses (total number of courses)
# E (Edges) = total number of prerequisite pairs in the input list

# Time Complexity : O(V + E) Why? Building Adjacency List O(E) + DFS (Visiting Vertices O(V) + Exploring Edges O(E))
# Space Complexity : O(V + E) Why? Adjacency List O(V + E), State Tracking Arrays (Visited and Path), Call Stack for Recursion O(V)


 