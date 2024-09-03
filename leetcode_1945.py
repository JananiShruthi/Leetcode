class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        d = {ch: i + 1 for i, ch in enumerate(alphabet)}
        ans1 = ''.join(str(d[ch]) for ch in s)
        
        for _ in range(k):
            result = sum(int(ch) for ch in ans1)
            if result < 10:
                return result
            ans1 = str(result)
            
        return result
