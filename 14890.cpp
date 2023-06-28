#include <iostream>
#include <vector>
using namespace std;

int cal(vector<vector<int>> map, int N, int L) {

    int cnt = 0;
    vector<vector<int>> hill(N + 1, vector<int>(N + 1, 0)); //���� ����

    for (int i = 1; i <= N; i++) {

        bool check = true;

        //���ʿ��� ������ �˻�
        for (int j = 1; j < N; j++) {

            if (map[i][j] > map[i][j + 1]) {

                //���� Ȯ��
                if (j + L > N) {
                    check = false;
                    break;
                }

                //���� ���� 1 Ȯ��
                for (int k = j + 1; k <= j + L; k++) {
                    if (map[i][k] != map[i][j] - 1) {
                        check = false;
                        break;
                    }

                    hill[i][k]++; //���� ���� 1�̸� ���� ���´�
                }

                if (check == false)
                    break;

                j += L - 1;
            }

        }

        //���ʺ��� �˻����� �� �̻������� �����ʺ��� �˻��� �ʿ� x
        if (check == false)
            continue;

        //�����ʿ��� �������� �˻�
        for (int j = N; j > 1; j--) {

            if (map[i][j] > map[i][j - 1]) {

                if (j - L < 1) {
                    check = false;
                    break;
                }

                for (int k = j - 1; k >= j - L; k--) {

                    //���� ���� �ȸ°ų� ���� �̹� ���� ������ ��
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

