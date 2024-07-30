class Solution {
public:
    int minimumDeletions(string s) {
        // the intution is if the current encountered char is a and bcount is not 0 ie b has already been encountered before a then increment mindel, and decrement bcount assuming that the previous b has been deleted.
        int bcount = 0;
        int mindel = 0;
        for(int i = 0; i < s.length();i++)
        {
            if (s[i] == 'b')
                bcount += 1;
            else
            {
                if(bcount > 0)
                {
                    mindel += 1;
                    bcount -= 1;
                }
            }
        }
        return mindel;
    }

};
