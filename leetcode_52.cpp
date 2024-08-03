class Solution {
public:
    int lengthOfLastWord(string s) {
        cout<<s.length();
        int n = s.length() - 1;
        int cnt = 0;
        int index = n;
        for(int i = n; i >=0; i--) //to start the index from the non widespace character from the last char of the string
        {
            if(s[i] != ' ')
            {
                index = i;
                break;
            }
        }
        for(int i = index; i>=0; i--)
        {
            if(s[i] != ' ')
            {
                cnt++;
            }
            else
            {
                break;
            }
        }
        cout<<"Length of the final word: "<<cnt;
        return cnt;
    }
};
