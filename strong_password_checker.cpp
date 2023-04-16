class Solution {
public:
    int lf = 0, digit = 0, lowf = 0, upf = 0, spf = 0, cnt = 5, s, u, l, d, len, adj = 0; 
    int length_pass(string pass)
    {
        if(pass.length() >= 6)
        {
            lf = 1;
        }
        return lf;
    }
    int isDigit(string pass)
    {
        int n = pass.length();
        for(int i = 0; i < n; i++)
        {
            if(isdigit(pass[i]))
            {
                digit = 1;
                break;
            }
        }
        return digit;
    }
    int lowercase(string pass)
    {
        int n = pass.length();
        for(int i = 0; i < n; i++)
        {
            if(islower(pass[i]))
            {
                lowf = 1;
                break;
            }
        }
        return lowf;
    }
    int uppercase(string pass)
    {
        int n = pass.length();
        for(int i = 0; i < n; i++)
        {
            if(isupper(pass[i]))
            {
                upf = 1;
                break;
            }
        }
        return upf;
    }
    int special_char(string pass)
    {
        int n = pass.length();
        for(int i = 0; i < n; i++)
        {
            if((pass[i] == '!') || (pass[i] == '@') || (pass[i] == '#') || (pass[i] == '$') || (pass[i] == '%') || (pass[i] == '^') || (pass[i] == '&') || (pass[i] == '*') || (pass[i] == '(') ||  (pass[i] == ')') || (pass[i] == '-') || (pass[i] == '+'))
            {
                spf = 1;
                break;
            }
        }
        return spf;
    }
    int adjacent(string pass)
    {
        for(int i = 0; i < pass.length(); i++)
        {
            if(i != pass.length() - 1)
            {
                if(pass[i] == pass[i + 1])
                {
                    adj = 1;
                }
            }
        }
        return adj;
    }
    
    bool strongPasswordCheckerII(string password) {
        int n = password.length();
        if(length_pass(password) && uppercase(password) && lowercase(password) && isDigit(password) && !adjacent(password) && special_char(password))
        {
            return true;

        }
        else
        {
            return false;
        }
    }
};
