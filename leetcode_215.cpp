class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minheap;
        for(int num : nums)
        {
            minheap.push(num);
            if(minheap.size() > k) // if the minheap size exceeds k remove the smallest ele which is nothing but the topmost element of the minheap
            {
                minheap.pop();
            }
        }
        return minheap.top();
    }
};
