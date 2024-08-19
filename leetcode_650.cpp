/* The approach taken to find the minimum no. of operations required to display the char n times is:
1) Divide the n by the prime factors until it becomes 1
2) Add the prime factors to a variable and that is the min steps required to display the char 'a' n times
*/

class Solution {
public:
    int minSteps(int n) {
        if(n == 1)
            return 0;

        int factor = 2;
        int ans = 0;
        while(n > 1)
        {
            while(n % factor == 0)
            {
                n = n / factor;
                ans += factor;
            }
            factor += 1;
        }
        return ans;
    }
};
