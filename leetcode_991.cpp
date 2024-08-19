/*
the intution is to reduce the target to the startVlaue. until startValue < target, if target is even, divide target by 2(reverse of mul by 2)
if its not even then add 1 to target(reverse of subracting 1). At the end the no.of steps would be steps + (startValue - target)
*/

class Solution {
public:
    int brokenCalc(int startValue, int target) {
        int steps = 0;
        while(startValue < target)
        {
            if(target % 2 == 0)
            {
                target /= 2;
            }
            else
            {
                target += 1;
            }
            steps += 1;
        }
        cout<<"No. of steps will be: "<<steps + (startValue - target);
        return steps + (startValue - target);
    }
};
