class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join(str(i) for i in range(k))
        
        # Start node consists of n-1 zeros
        start_node = "0" * (n - 1)
        
        # Keep track of visited directed edges (node + edge_digit)
        visited = set()
        result = []
        
        def dfs(node):
            for x in range(k):
                edge = node + str(x)
                if edge not in visited:
                    visited.add(edge)
                    # Next node is the suffix of length n - 1
                    dfs(edge[1:])
                    result.append(str(x))
                    
        dfs(start_node)
        
        # The result is built in reverse during DFS, append the start_node at the end
        return "".join(result) + start_node
        