class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0
        cnt = 1
        
        if n == 1:
            return 1  # FIX #1: return the length
        
        for i in range(n-1):
            if chars[i] == chars[i+1]:
                cnt += 1
            else:
                chars[write] = chars[i]
                write += 1
                if cnt > 1:  # FIX #3 & #4: only write count if > 1
                    for digit in str(cnt):
                        chars[write] = digit
                        write += 1
                cnt = 1
        
        # FIX #2: Handle the last group
        chars[write] = chars[n-1]
        write += 1
        if cnt > 1:
            for digit in str(cnt):
                chars[write] = digit
                write += 1
        
        return write
