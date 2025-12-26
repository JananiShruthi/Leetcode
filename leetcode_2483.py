class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        min_penalty = penalty
        answer = 0
        for i , c in enumerate(customers):
            if c == 'Y': # shop should be open
                penalty -= 1
            else:
                penalty += 1
            
            if min_penalty > penalty:
                min_penalty = penalty
                answer = i + 1
        return answer
