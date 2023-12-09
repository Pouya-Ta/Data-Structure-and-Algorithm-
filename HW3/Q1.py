import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

# Build adjacency list
adj = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

# For each vertex v
result = []
for v in range(n):
    p, e = a[v], 0 # Initialize prices
    visited = set([v]) # Set of visited vertices
    ns = [] # Priority queue to store neighbors of v
    for u in adj[v]:
        if u not in visited: # If neighbor u has not been visited
            heapq.heappush(ns, (a[u], u)) # Add u to the priority queue
    while ns: # Process all vertices connected to v
        u = heapq.heappop(ns)[1] # Get the cheapest unvisited neighbor of v
        if u not in visited: # If neighbor u has not been visited
            visited.add(u) # Mark u as visited
            for w in adj[u]: # Iterate over neighbors of u
                if w not in visited: # If neighbor w has not been visited
                    heapq.heappush(ns, (a[w], w)) # Add w to the priority queue
            if a[u] < p + e: # If buying at the price of u is cheaper than renting
                p += a[u] # Buy at the price of u
            else: # Otherwise, rent at the price of u
                e += a[u] - (p + e) + 1
                p += a[u]
    result.append(str(e)) # Add the result to the list of results

# Print the results
print('\n'.join(result))
