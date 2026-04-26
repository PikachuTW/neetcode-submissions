class Solution {
public:
    int jump(vector<int>& nums) {
        int l = 0, r = 0;
        int count = 0;
        while(l < nums.size() - 1 && r < nums.size() - 1){
            int mm = l;
            for(int i = l;i<=r;i++){
                mm = max(i + nums[i], mm);
            }
            l = r + 1, r = mm;
            count += 1;
        }
        return count;
    }
};
