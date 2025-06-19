class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        temp = 0
        for i in range(len(timeSeries)-1):
            temp = timeSeries[i] + (duration - 1)
            print("Temp: ", temp)
            if temp < timeSeries[i+1]:
                print("No overlap")
                ans += duration
            else:
                print("Overlap")
                ans += min(duration, timeSeries[i+1] - timeSeries[i])

            print("Ans: ",ans)

        if temp <= timeSeries[-1]:
            ans += duration
        else:
            ans += duration

        print("Ans:", ans)
        return ans
