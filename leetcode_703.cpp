class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for(int num : nums) {
            add(num); // Use the add function to populate the min-heap
        }
    }
    
    int add(int val) {
        if (minHeap.size() < k) { // if the no.of elements to be added is lesser than k, then there is still room left to add more elements.
            minHeap.push(val);
        } else if (val > minHeap.top()) { // if the current incoming val is greater than top of minheap(the smallest element) then this ele could be in the kth largest so remove the top and add the val to the min heap
            minHeap.pop();
            minHeap.push(val);
        }
        return minHeap.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
