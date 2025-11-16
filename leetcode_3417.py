class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        answer = []
        l = []
        for i in range(len(grid)):
            if i%2 != 0:
                l.extend(grid[i][::-1])
            else:
                l.extend(grid[i])
        for i in range(0, len(l), 2):
            answer.append(l[i])

        return answer
