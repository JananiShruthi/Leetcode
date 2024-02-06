def pick_numbers(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
        

nums = list(map(int, input().split()))
target = int(input("Enter the target:"))
res = pick_numbers(nums, target)
print(res)
