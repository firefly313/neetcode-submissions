class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## basically we need to check cycles
        ## dfs helper
        def dfs(node):
            ## theres a cycle 
            if node in path:
                return False
            ## 
            if node in visited:
                return True

            path.add(node)

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            
            path.remove(node)
            visited.add(node)

            return True
        
        ## can make adjacency list
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            if a == b:
                return False
            adj[a].append(b)
        
        visited = set()
        path = set()

        ## base cases
        if numCourses == 1 or len(prerequisites) == 0:
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        
        return True