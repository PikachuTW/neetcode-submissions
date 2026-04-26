/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), [&](Interval a, Interval b){
            return a.start < b.start;
        });
        multiset<int> s;
        for(auto& el: intervals){
            auto ub = upper_bound(s.begin(), s.end(), el.start);
            if (ub == s.begin()) {
                s.insert(el.end);
            }else{
                ub--;
                s.erase(ub);
                s.insert(el.end);
            }
        }
        return s.size();
    }
};
