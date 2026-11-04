from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        # Track graph and degrees
        graph = defaultdict(list)
        out_degree = defaultdict(int)
        in_degree = defaultdict(int)
        
        for u, v in pairs:
            graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1
            
        # Find the start node for the Eulerian path
        start_node = pairs[0][0]
        for node in out_degree:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
                
        # Iterative Hierholzer's Algorithm using a stack
        stack = [start_node]
        path = []
        
        while stack:
            curr = stack[-1]
            if graph[curr]:
                # Visit the next destination
                next_node = graph[curr].pop()
                stack.append(next_node)
            else:
                # No more outgoing edges, record the node
                path.append(stack.pop())
                
        # Path is built in reverse, so reverse it back
        path.reverse()
        
        # Reconstruct the pairs from the node sequence
        return [[path[i], path[i + 1]] for i in range(len(path) - 1)]