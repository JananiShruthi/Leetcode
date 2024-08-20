class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            val = target - num
            if val in nums:
                if(i != nums.index(val)):
                    return [i, nums.index(val)]

''' The following is the program in cpp 
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> num_map; // to store value and its index
    for (int i = 0; i < nums.size(); i++) {
        int val = target - nums[i]; // calculate the complement
        if (num_map.find(val) != num_map.end()) { // if complement exists in the map
            return {num_map[val], i}; // return indices
        }
        num_map[nums[i]] = i; // store value and its index
    }
    return {}; // return empty vector if no solution found
}
'''
