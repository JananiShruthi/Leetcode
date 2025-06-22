class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        d = {}
        ans = 0
        print(count)
        for i,n in enumerate(nums):
            d[(i,n)] = k - n
        for key,val in d.items():
            key_flag = 0
            val_flag = 0
            if count[key[1]] > 0:
                #nums.remove(key[1])
                count[key[1]] -= 1
                key_flag = 1
            if count[val] > 0:
                #nums.remove(val)
                count[val] -= 1
                val_flag = 1
            if key_flag == val_flag == 1:
                ans += 1
        return ans
