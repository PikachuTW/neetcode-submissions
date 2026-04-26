class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> arr;
        for(int i = 0;i<nums.size();i++){
            arr.emplace_back(nums[i], i);
        }
        sort(arr.begin(), arr.end());
        int left = 0, right = nums.size() - 1;
        while(true){
            int sum = arr[left].first + arr[right].first;
            if (sum > target){
                right--;
            }else if (sum < target){
                left++;
            }else{
                if (arr[left].second > arr[right].second) {
                    swap(arr[left].second, arr[right].second);
                }
                return vector<int>({arr[left].second, arr[right].second});
            }
        }
    }
};
