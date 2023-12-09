from collections import deque

# This function performs a breadth-first search (BFS) on the given graph
def bfs(adj, s, dest, v):
    # Initialize arrays A and B
    A = [-1] * v  # Stores the shortest path from s to dest
    B = [float('inf')] * v  # Stores the distance from s to each vertex in the graph

    # Initialize visited array and queue for BFS
    visited = [False] * v
    queue = deque()

    # Mark source node as visited, set its distance to 0, and add it to the queue
    visited[s] = True
    B[s] = 0
    queue.append(s)

    # Perform BFS
    while queue:
        # Dequeue the front node from the queue
        u = queue.popleft()
        # Explore all adjacent nodes of the dequeued node
        for i in adj[u]:
            if not visited[i]:
                # Mark the adjacent node as visited, set its distance, and add it to the queue
                visited[i] = True
                B[i] = B[u] + 1
                A[i] = u
                queue.append(i)
                # If the destination node is found, return True
                if i == dest:
                    return True
    # If the destination node was not found, return False
    return False

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read n, m, s, and t for this test case
    n, m, s, t = map(int, input().split())
    # Create an adjacency list for the graph
    adj = [[] for i in range(n)]
    # Read m pairs of vertices that have an edge between them
    for i in range(m):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
    # Decrement s and t by 1 to match 0-based indexing
    s -= 1
    t -= 1
    # Run BFS on the graph and get the shortest distance from s to t
    dist = bfs(adj, s, t, n)
    # If there is no path from s to t, print -1
    if not dist:
        print(-1)
    else:
        # Otherwise, reconstruct the shortest path using array A and print its length
        path = []
        crawl = t
        path.append(crawl)
        while A[crawl] != -1:
            path.append(A[crawl])
            crawl = A[crawl]
        print(B[t])
