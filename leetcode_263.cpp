class Solution {
public:
    bool isUgly(int n) {
        priority_queue<long, vector<long>, greater<long>> minHeap;
        unordered_set<long> seen; // To avoid duplicates
        minHeap.push(1); // first ugly number
        seen.insert(1);

        vector<int> primes = {2,3,5};
        while(true)
        {
            long uglynum = minHeap.top();
            if(uglynum == n)
            {
                return true;
            }
            else if(uglynum > n)
            {
                return false;
            }
            minHeap.pop();
            for(int p:primes)
            {
                long newuglynum = uglynum * p;
                if(seen.find(newuglynum) == seen.end())
                {
                    seen.insert(newuglynum);
                    minHeap.push(newuglynum);
                }
            }
        }
    }
};
