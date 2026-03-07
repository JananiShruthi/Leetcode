class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        odd = {}
        even = {}

        for i, n in enumerate(nums):
            if i % 2 == 0:
                even[n] = even.get(n, 0) + 1
            else:
                odd[n] = odd.get(n, 0) + 1

        print(f"Even: {even}")
        print(f"Odd: {odd}")
        # get top two for even
        even_items = sorted(even.items(), key=lambda x: x[1], reverse=True)
        odd_items = sorted(odd.items(), key=lambda x: x[1], reverse=True)

        print(f"even_items: {even_items} and odd_items: {odd_items}")
        max_even = even_items[0]
        max_odd = odd_items[0]

        second_even = even_items[1] if len(even_items) > 1 else (None, 0)
        second_odd = odd_items[1] if len(odd_items) > 1 else (None, 0)

        if max_even[0] != max_odd[0]:
            ans = len(nums) - max_even[1] - max_odd[1]
        else:
            option1 = len(nums) - max_even[1] - second_odd[1]
            option2 = len(nums) - second_even[1] - max_odd[1]
            ans = min(option1, option2)

        return ans
