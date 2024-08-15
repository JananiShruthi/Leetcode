class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0;
        int ten = 0;
        for(int i = 0; i < bills.size(); i++)
        {
            if(bills[i] == 5)
            {
                five++;
            }
            else if(bills[i] == 10)
            {
                if(five > 0)
                {
                    five--; // we give the 5 dollars as change
                    ten++;
                }
                else // we dont have five dollars to give the change
                {
                    return false;
                }
            }
            else if(bills[i] == 20)
            {
                if(five >= 1 && ten >= 1)
                {
                    five--;
                    ten--;
                } 
                else if(five >= 3) // remaining 15 can be given as a change to 3, 5rs
                {
                    five -= 3;
                }
                else // can't give the change
                {
                    return false;
                }
            }
        }
        return true;
    }
};
