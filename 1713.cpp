#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct str {
    int num;
    int vote;
    int times;
    str(int num, int vote, int times) :num(num), vote(vote), times(times) {};
};

bool operator<(str s1, str s2) {
    //투표 적은 순, 동일하면 먼저 들어온 순으로
    if (s1.vote == s2.vote)
        return s1.times > s2.times;
    else
        return s1.vote > s2.vote;
}
int main() {

    std::ios_base::sync_with_stdio(false);

    int photo_size;
    int T = 0;
    cin >> photo_size >> T;

    int recommend_num = 0;
    vector<int> exists(101, 0); //추천 유무
    vector<str> vec;

    for (int testCase = 1; testCase <= T; testCase++) {
        cin >> recommend_num;

        //해당 후보 이전에 추천 받았을 때
        if (exists[recommend_num]) {

            for (int i = 0; i < vec.size(); i++) {
                if (vec[i].num == recommend_num) {
                    vec[i].vote += 1; //투표수 증가
                    break;
                }
            }
            continue;
        }

        exists[recommend_num]++;
        if ((int)vec.size() < photo_size) { //아직 사진틀 여유 있으면
            vec.push_back(str(recommend_num, 1, testCase));
            continue;
        }


        priority_queue<str> pq;
        for (int i = 0; i < vec.size(); i++) {
            pq.push(vec[i]);
        }

        str s = pq.top();
        for (int i = 0; i < vec.size(); i++) {
            if (vec[i].num == s.num) {
                exists[s.num] = 0;
                vec[i].num = recommend_num;
                vec[i].vote = 1;
                vec[i].times = testCase;
                break;
            }
        }
    }

    vector<int> ans;
    for (int i = 0; i < vec.size(); i++) {
        ans.push_back(vec[i].num);
    }

    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); i++)
        cout << ans[i] << " ";

    return 0;
}
