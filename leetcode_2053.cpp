class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> umap;
        int val = 1;
        string ans;
        //initialising the unordered map with 0
        for(int i = 0; i < arr.size(); i++)
        {
            umap[arr[i]] = 0;
        }
        for(int i = 0; i < arr.size(); i++)
        {
            cout<<"String: "<<arr[i]<<endl;
            umap[arr[i]] += 1;
        }
        for(int i = 0; i < arr.size(); i++)
        {
            if(umap[arr[i]] == 1)
            {
                if(val == k)
                {
                    ans = arr[i];
                    break;
                }
                else
                {
                    val += 1;
                }
            }
        }
        cout<<"Answer string: "<<ans;
        return ans;
    }
};
