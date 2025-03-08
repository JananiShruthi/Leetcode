# This approach of sliding window is great.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = blocks[:k].count('W')  # Count 'W's in the first window
        min_colour = w_count  # Initialize minimum repaint count
        
        for i in range(1, len(blocks) - k + 1):  
            # Slide window: Remove left char, add right char
            if blocks[i - 1] == 'W':
                w_count -= 1  
            if blocks[i + k - 1] == 'W':
                w_count += 1  
            
            min_colour = min(min_colour, w_count)  # Update min
        
        return min_colour
