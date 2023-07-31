'''Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.'''

'''APPROACH: rotate a matrix 0-90-180-270 at any one of the rotation the mat will be matching the target'''
class Solution(object):
    def rotate(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in mat:
            i.reverse()

    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        if mat == target:
            return True
        for i in range(0, 3): #rotate a matrix 0->90->180->270
            self.rotate(mat)
            if mat == target:
                return True
        return False


