class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(1,n+1))
        print("[INITIAL LIST OF PERSONS] ", l)
        k = k - 1
        print("[K] : ", k)
        i = 0
        if len(l) == 1:
            return l[0]
        while l:
            i = (i + k)%len(l)
            print("[PERSON] ", i)
            l.remove(l[i])
            print("LIST: ", l)

            if len(l) == 1:
                return l[0]
