class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## helper dfs function
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        ## make adjacency list for
        ## the given edges
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        connected = 0

        ## loop 
        for node in range(n):
            if node not in visited:
                connected += 1
                dfs(node)
        
        ## return
        return connected