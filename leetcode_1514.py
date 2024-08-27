# The negative value of probability is stored becoz we are using minheap by default and storing the original +ve value will make the heap mush the element down 

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for index, e in enumerate(edges):
            u,v = e
            graph[u].append((v, succProb[index]))
            graph[v].append((u, succProb[index]))

        print("The graph is: ", graph)

      # The following is nothing but the dijiksta's maximum distance implementation

        pq = [(-1, start_node)]
        distances = {node: -math.inf for node in graph}
        distances[start_node] = 0
        
        while pq:
            cur_dist, cur_node = heapq.heappop(pq)
            cur_dist = -cur_dist # convert back to positive
            
            if cur_node == end_node:
                print("Distances: ", distances)
                return cur_dist
            
            for neighbor, weight in graph[cur_node]:
                distance = cur_dist * weight
                if distance > distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (-distance, neighbor))

        # If the goal node is unreachable, return -1 or some indicator
        return 0
