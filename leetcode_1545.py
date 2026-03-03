class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = {0: "0"}
        for i in range(1,n+1):
            inv = ''.join('1' if c == '0' else '0' for c in s[i-1])
            s[i] = s[i-1] + "1" + inv[::-1]
            if len(s[i]) > (k-1):
                # instead of calculating till the nth string and returning the kth bit, 
                # we just check if the last calculated string has exceeded the length of k-1, 
              ` # if so we just return from that string itself, no need to process till nth number
                return s[i][k-1]
