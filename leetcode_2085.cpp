class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        unordered_map<string, int> umap1;
        unordered_map<string, int> umap2;
        vector<string> v;
        int ans = 0;
        //initialise the unorderd map for both the vectors
        for(int i = 0; i < words1.size(); i++)
        {
            umap1[words1[i]] = 0;
        }
        for(int i = 0; i < words2.size(); i++)
        {
            umap2[words2[i]] = 0;
        }
        for(int i = 0; i < words1.size(); i++)
        {
            umap1[words1[i]] += 1;
        }
        for(int i = 0; i < words2.size(); i++)
        {
            umap2[words2[i]] += 1;
        }
        int len = min(words1.size(), words2.size());
        if (words1.size() < words2.size())
        {
            v = words1;
        }
        else
        {
            v = words2;
        }
        for(int i = 0; i < len; i++)
        {
            if(umap1[v[i]] == 1 && umap2[v[i]] == 1)
            {
                ans++;
            }
        }
        cout<<ans<<endl;
        return ans;

    }
};
