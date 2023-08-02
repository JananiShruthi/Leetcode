'''Given a string s, find the length of the longest substring
 without repeating characters.'''

class Solution:
    def isValid(self, s):
        for i in s:
            if(s.count(i) > 1):
                return -1
        return 1

    def lengthOfLongestSubstring(self, ip: str) -> int:
        n = len(ip)
        maxi = 0
        max_str = ""

        for i in range(n):
            s = ""
            for j in range(i, n):
                s += ip[j]
                v = self.isValid(s)
                if(v == 1):
                    if(len(s) > maxi):
                        maxi = len(s)
                        max_str = s

        #print("Maximum possible substring: ", max_str)
        return len(max_str)

  '''986 / 987 testcases passed'''
