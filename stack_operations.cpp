class CustomStack {
    int size;
    vector<int> stack;
public:
    CustomStack(int maxSize) {
        size = maxSize;
    }
    
    void push(int x) {
        if (stack.size() < size)
        {
            stack.push_back(x);
        }
    }
    
    int pop() {
        if(stack.size() == 0)
        {
            return -1;
        }
        else
        {
            int ele = stack.back();
            stack.pop_back();
            return ele;
        }
    }
    
    void increment(int k, int val) {
        if(k >= stack.size())
        {
            for(int i = 0; i < stack.size(); i++)
            {
                stack[i] += val;
            }
        }
        else 
        {
            for(int i = 0; i < k; i++)
            {
                stack[i] += val;
            }
        }

    }
};
