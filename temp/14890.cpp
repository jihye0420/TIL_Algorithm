#include <iostream>
#include <vector>
using namespace std;

int cal(vector<vector<int>> map, int N, int L) {

    int cnt = 0;
    vector<vector<int>> hill(N + 1, vector<int>(N + 1, 0)); //경사로 구간

    for (int i = 1; i <= N; i++) {

        bool check = true;

        //왼쪽에서 오른쪽 검사
        for (int j = 1; j < N; j++) {

            if (map[i][j] > map[i][j + 1]) {

                //범위 확인
                if (j + L > N) {
                    check = false;
                    break;
                }

                //높이 차이 1 확인
                for (int k = j + 1; k <= j + L; k++) {
                    if (map[i][k] != map[i][j] - 1) {
                        check = false;
                        break;
                    }

                    hill[i][k]++; //높이 차이 1이면 경사로 짓는다
                }

                if (check == false)
                    break;

                j += L - 1;
            }

        }

        //왼쪽부터 검사했을 때 이상있으면 오른쪽부터 검사할 필요 x
        if (check == false)
            continue;

        //오른쪽에서 왼쪽으로 검사
        for (int j = N; j > 1; j--) {

            if (map[i][j] > map[i][j - 1]) {

                if (j - L < 1) {
                    check = false;
                    break;
                }

                for (int k = j - 1; k >= j - L; k--) {

                    //높이 차이 안맞거나 경사로 이미 지은 구간일 때
                    if (map[i][k] != map[i][j] - 1 || hill[i][k]) {
                        check = false;
                        break;
                    }
                }

                if (check == false)
                    break;

                j -= L - 1;
            }
        }

        if (check)
            cnt++;
    }

    return cnt;
}
int main() {

    int N, L;
    cin >> N >> L;

    int ans = 0;
    vector<vector<int>> horizon_road(N + 1, vector<int>(N + 1, 0)); //(i,j)
    vector<vector<int>> vertical_road(N + 1, vector<int>(N + 1, 0)); //(j,i)

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            scanf("%d", &horizon_road[i][j]);
            vertical_road[j][i] = horizon_road[i][j];
        }
    }

    ans += cal(horizon_road, N, L);
    ans += cal(vertical_road, N, L);

    cout << ans << endl;

    return 0;
}

