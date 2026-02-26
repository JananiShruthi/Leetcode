class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = []
        for i in arr:
            num = i
            d.append([i, 0])
            while num >= 1:
                if num%2 == 1:
                    d[-1][1] += 1
                num = num // 2

        print(d)
        sorted_list = sorted(d, key=lambda item: (item[1], item[0]))
        print(f"sorted_list: {sorted_list}")
        
        return [x[0] for x in sorted_list]
