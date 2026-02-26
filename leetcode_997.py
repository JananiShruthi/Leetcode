class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:        
        people = set()
        trusting_list = []
        d = {}
        for i in range(n):
            people.add(i+1)

        for p in people:
            d[p] = []

        print(d)

        for t in trust:
            d[t[1]].append(t[0]) # create a hashmap with who all trusts the key
            trusting_list.append(t[0])
        
        if len(set(trusting_list)) == n: # everybody trusts somebody so no town judge
            return -1
        else: # Town judge exists
            for key, val in d.items():
                if len(val) == n - 1:
                    return key
        return -1
