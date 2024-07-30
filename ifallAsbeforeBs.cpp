class Solution {
public:
    bool checkString(string s) {
        int bcount = 0;
        for(char c :  s)
        {
            if (c == 'a')
            {
                if(bcount) // if there is some b before a
                    return false;
            }
            else
            {
                bcount++;
            }
        }
        return true;
    }
};
