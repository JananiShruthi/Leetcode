class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substrs = set()
        print(f"We need to have {pow(2,k)}")
        for i in range(len(s)):
            if len(s[i:i+k]) == k:
                substrs.add(s[i:i+k])

        print(substrs)
        print(len(substrs))
        if len(substrs) == pow(2,k):
            return True
        else:
            return False
