class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        for i in arr:
            num = i
            d[i] = 0
            while num >= 1:
                if num%2 == 1:
                    d[i] += 1
                num = num // 2
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
        print(f"Sorted dict: {sorted_dict}")
        ans = [key for key in sorted_dict.keys()]
        print(ans)
        return ans
