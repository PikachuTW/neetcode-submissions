class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        bool dp[5000] = {false};
        dp[0] = true;
        for(int i = 0;i<s.size();i++){
            if (!dp[i]) continue;
            for(string& word: wordDict){
                if (i + word.size() > s.size())continue;
                bool startsWith = true;
                for(int p = 0; p < word.size(); p++){
                    if (s[i + p] != word[p]){
                        startsWith = false;
                        break;
                    }
                }
                if (startsWith){
                    dp[i + word.size()] = true;
                }
            }
        }
        return dp[s.size()];
    }
};
