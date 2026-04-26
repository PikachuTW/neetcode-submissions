class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        string ans;
        for(int i = 0;i<n;i++){
            int left = i, right = i;
            while(true){
                if (s[left - 1] == s[right + 1] && left - 1 >= 0 && right + 1 < n){
                    left--;
                    right++;
                }else{
                    break;
                }
            }
            int len = right - left + 1;
            if (len > ans.size()){
                string newStr(s.begin() + left, s.begin() + right + 1);
                ans = newStr;
            }
        }
        for(int i = 0;i<n - 1;i++){
            int left = i, right = i + 1;
            if (s[left] != s[right])continue;
            while(true){
                if (s[left - 1] == s[right + 1] && left - 1 >= 0 && right + 1 < n){
                    left--;
                    right++;
                }else{
                    break;
                }
            }
            int len = right - left + 1;
            if (len > ans.size()){
                string newStr(s.begin() + left, s.begin() + right + 1);
                ans = newStr;
            }
        }
        return ans;
    }
};
