/*
The intution is create a minheap to pop out the nth ugly num, set to maintain the ugly nos that are processed(and to remove the duplicates)
pop the uglynum of the top from minheap and create all next possible uglynumbers by multiplying with 2, 3, 5 and push them into the heap if that num is already not in seen set. 
By repetitively doing so for n times we can extract the nth ugly num that is the top of the minheap.
*/

class Solution {
public:
    int nthUglyNumber(int n) {
        priority_queue<long, vector<long>, greater<long>> minHeap;
        unordered_set<long> seen; // To avoid duplicates
        minHeap.push(1); // first ugly number
        seen.insert(1);

        vector<int> primes = {2,3,5};
        long uglynum = 1;
        // now generate the next ugly number
        for(int i = 1; i < n; i++) // 1 to n since '1' is already pushed in minHeap
        {
            uglynum = minHeap.top();
            minHeap.pop();
            for(int p : primes)
            {
                long newuglynum = uglynum * p;
                if(seen.find(newuglynum) == seen.end())
                {
                    seen.insert(newuglynum);
                    minHeap.push(newuglynum);
                }
            }
        }
        return (int)minHeap.top();
    }
};
