class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans = {-1, -1};
        vector<int> occurance;
        int left = 0;
        int right = nums.size() - 1;

        for(int i = 0; i < nums.size(); i++)
        {
            if(nums[i] == target)
            {
                occurance.push_back(i);
            }
        }
        if(occurance.size() > 0)
        {
            ans[0] = occurance[0];
            ans[1] = occurance[occurance.size() - 1];
        }

        return ans;
    }
};
