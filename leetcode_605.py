class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        ans = 0

        if length == 1:
            if flowerbed[0] == 0:
                ans += 1
        else:
            if flowerbed[0] == 0 == flowerbed[1] == 0:
                ans += 1
                flowerbed[0] = 1

        for i in range(1, length-1):
            if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
                ans +=1
                flowerbed[i] = 1

        if flowerbed[length-2] == flowerbed[length-1] == 0:
            ans += 1
            flowerbed[length-1] = 1
            
        print("flowerbed: ",flowerbed)
        print("ans: ",ans)
        if ans >= n:
            return True
        else:
            return False
