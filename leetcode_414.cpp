/* we consider only the unique elements becoz in the list [2,2,3,1] 
the 3rd max elemnt is 1 if we dont consider only the unique elements we will get the answer as 2 */

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int k = 3;
        set<int> uniquenums(nums.begin(), nums.end()); // we need only the unique elements 
        if(uniquenums.size() < 3) // if the number of unique elements is less than 3 
        {
            return *max_element(uniquenums.begin(), uniquenums.end());
        }
        cout<<"K: "<<k;
        priority_queue<int, vector<int>, greater<int>> minheap;
        for(int n : uniquenums)
        {
            minheap.push(n);
            if(minheap.size() > k)
            {
                minheap.pop();
            }
        }
        return minheap.top();
    }
};
