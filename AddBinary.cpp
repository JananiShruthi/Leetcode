class Solution {
public:
    string addBinary(string a, string b) {
        int n1 = a.size();
        int n2 = b.size();
        int a1, b1, ans = 0;
        char c = '0';
        string out = "";
        if(n1 < n2)
        {
            swap(a,b);
        }
        while(b.size() < a.size())
        {
            b = "0" + b;
        }
        for(int i = b.size() - 1; i>= 0; i--)
        {
            if(a[i] == '1' && b[i] == '1' && c == '0')
            {
                out = "0" + out;
                c = '1';
            }
            else if(a[i] == '1' && b[i] == '0' && c == '0')
            {
                out ="1" + out;
                c = '0';
            }
            else if(a[i] == '0' && b[i] == '0' && c == '0')
            {
                out ="0" + out;
                c = '0';
            }
            else if(a[i] == '0' && b[i] == '1' && c == '0')
            {
                out ="1" + out;
                c = '0';
            }
            else if(a[i] == '0' && b[i] == '0' && c == '1')
            {
                out ="1" + out;
                c = '0';
            }else if(a[i] == '0' && b[i] == '1' && c == '1')
            {
                out ="0" + out;
                c = '1';
            }else if(a[i] == '1' && b[i] == '1' && c == '1')
            {
                out="1"+ out;
                c = '1';
            }else if(a[i] == '1' && b[i] == '0' && c == '1')
            {
                out="0"+ out;
                c = '1';
            }
        }
        if(c == '1')
        {
            out = "1" + out;
        }
        return out;
    }
};
