class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        answer = 0
        for i in range(k):
            if happiness[i] - i > 0:
                answer += (happiness[i] - i)
        return answer
