class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l = s1.split() + s2.split()
        print(l)
        return [val for val in l if l.count(val) == 1]
