class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_count = 0
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            
            if count >= max_count:
                max_count = count
        return max_count

# used sliding window. expand the window on the right side and decrease the window on the left side. Sice counter is what matters to us here. we are reducing and incrementing the count. 
