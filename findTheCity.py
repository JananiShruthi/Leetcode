'''There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
'''

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # computing the possibility of reaching every node and their weights: 
        dist = [[float('inf')] * n for _ in range(n)]
        weights = {}
        # Distance to itself is 0
        for i in range(n):
            dist[i][i] = 0
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        for i in range(len(dist)):
            weights[i] = 0
            print(dist[i])
            for j in range(len(dist)):
                if dist[i][j] <= distanceThreshold and dist[i][j] != 0:
                    weights[i] += 1


        print(weights)
        print(min(weights.values()))
        return max([key for key,val in weights.items() if val == min(weights.values())])
