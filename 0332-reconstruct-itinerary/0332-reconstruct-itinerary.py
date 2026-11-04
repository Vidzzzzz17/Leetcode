from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Build the graph using min-heaps for each departure airport
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
            
        route = []
        
        def dfs(airport):
            # Visit all outgoing edges in lexicographical order
            while graph[airport]:
                next_dest = heapq.heappop(graph[airport])
                dfs(next_dest)
            # Add to route once no more outgoing flights are left
            route.append(airport)
            
        dfs("JFK")
        
        # Since we append after exhausting flights, the route is reversed
        return route[::-1]