''' Centre of a graph is nothing but a node where all the other nodes of a graph is connected to. Te edges of a graph is given in a list: 
[[1,2],[2,3],[4,2]] - here all the nodes are connected to the node 2 hence the centre of the star tree is 2'''
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1 # number of nodes in the graph
        nodes = list(range(1, n+1))
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            centre = edges[0][0]
        elif edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            centre = edges[0][1]

        print("[CENTRE]: ", centre)
        return centre
