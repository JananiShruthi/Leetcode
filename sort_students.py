'''Input: score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2
Output: [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
Explanation: In the above diagram, S denotes the student, while E denotes the exam.
- The student with index 1 scored 11 in exam 2, which is the highest score, so they got first place.
- The student with index 0 scored 9 in exam 2, which is the second highest score, so they got second place.
- The student with index 2 scored 3 in exam 2, which is the lowest score, so they got third place.'''

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        final = []
        kl = [(index, row[k]) for index, row in enumerate(score)]
        print(kl)
        sort_kl = sorted(kl, key = lambda x : x[1], reverse = True)
        print(sort_kl)
        for index, rowval in sort_kl:
            final.append(score[index])
        print("[FINAL]", final)
        return final
