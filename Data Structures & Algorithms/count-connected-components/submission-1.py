class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        ## creating an adjacency list
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        ## base case 
        if edges is None or n == 0:
            return 0

        connected = 0
        visited = set()

        for node in range(n):
            if node not in visited:
                connected += 1
                dfs(node)


        return connected

        ## wrong approach but good thinking V

        ## should look at each edge
        ## start with +1
        ## if [left1][right1] [left2][right2] 
        ## check if right1 == left2, if yes then skip
        ## if not add 1 to num connected

        #i = 0
        #j = 1

        #edges = sorted(edges)
        #print(edges)

        #for _ in range(len(edges)+1):
            #if j >= len(edges):
                #break
            #if edges[i][1] != edges[j][0]:
                #connected += 1
            #i += 1
            #j += 1
            
        #return connected

    ## always want to look at right and left to compare

    #compare:
    #[0][1] with [1][0]
    #[1][1] with [2][0]
    #[2][1] with [3][0]
