# This is how you should do a sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            # Shrink the window from the left until we have all unique characters
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set
            char_set.add(s[right])
            
            # Update the answer if we found a longer substring
            ans = max(ans, right - left + 1)

        return ans
