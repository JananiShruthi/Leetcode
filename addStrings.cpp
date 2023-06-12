/*Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must a
lso not convert the inputs to integers directly.*/

class Solution {
public:
    string addStrings(string num1, string num2) {
        int l1 = num1.length();
        int l2 = num2.length();
        int carry = 0, val;
        string ans = "";
        string result = "";
        if(l1 < l2)//making the length of both the strings same
        {
            int num_0s = l2 - l1;
            for(int i = 0; i < num_0s; i++)
            {
                num1 = "0" + num1;

            }
        }
        else
        {
            int num_0s = l1 - l2;
            for(int i = 0; i < num_0s; i++)
            {
                num2 = "0" + num2;
            }
        }
        cout<<"num1: "<<num1<<endl<<"num2: "<<num2<<endl;
        for(int i = num1.length() - 1; i >= 0; i--)
        {
            val = ((int)num1[i]-'0')+((int)num2[i]-'0')+carry;
            if(val > 9)
            {
                carry = val / 10;
                val = val % 10;
            } 
            else
            {
                carry = 0;
            }
            ans += to_string(val);
        }
        if(carry != 0)
        {
            ans += to_string(carry);
        }
        cout<<ans<<endl;
        /*int len = ans.length();
        for(int i = 0; i < len; i++)
        {
            result[i] = ans[len - i - 1];
        }
        cout<<result;*/
        for (int i = ans.length() - 1; i >= 0; i--)
            result += ans[i];
                
        return result;
    }
};
