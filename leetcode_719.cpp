// The solution is implemented with the binary search. 

class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        // Sort the array first
        sort(nums.begin(), nums.end());

        // Define the search space for the smallest distance
        int left = 0;
        int right = nums.back() - nums.front();

        // Binary search on the distance
        while (left < right) {
            int mid = left + (right - left) / 2;

            // Count how many pairs have a distance <= mid
            int count = 0;
            int j = 0;
            for (int i = 0; i < nums.size(); i++) {
                while (j < nums.size() && nums[j] - nums[i] <= mid) {
                    j++;
                }
                count += j - i - 1;
            }

            // Adjust the binary search range based on the count
            if (count >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
};
