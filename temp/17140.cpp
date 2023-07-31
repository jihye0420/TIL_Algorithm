#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;
#define N 100

int Y = 3;
int X = 3;
vector<vector<int>> map;

struct str {
    int value;
    int cnt;

    str(int value, int cnt) :value(value), cnt(cnt) {};
};

bool operator<(str s1, str s2) {
    if (s1.cnt != s2.cnt)
        return s1.cnt < s2.cnt;
    else
        return s1.value < s2.value;

}
int main() {

    int r, c, k;
    cin >> r >> c >> k;

    map = vector<vector<int>>(N, vector<int>(N, 0));

    for (int i = 0; i < Y; i++)
        for (int j = 0; j < X; j++)
            cin >> map[i][j];


    int ans = 0;
    while (true) {

        if (map[r - 1][c - 1] == k)
            break;

        if (ans > 100) {
            ans = -1;
            break;
        }

        int num[101] = { 0 };

        //R연산
        if (Y >= X) {
            for (int y = 0; y <= Y; y++) {

                memset(num, 0, sizeof(num));
                for (int x = 0; x <= X; x++) {
                    num[map[y][x]]++;
                    map[y][x] = 0;
                }

                vector<str> vec;
                for (int i = 1; i <= N; i++) {
                    if (num[i]) {
                        vec.push_back(str(i, num[i]));
                    }
                }

                sort(vec.begin(), vec.end());
                for (int i = 0, k = 0; i < vec.size(); i++, k += 2) {
                    map[y][k] = vec[i].value;
                    map[y][k + 1] = vec[i].cnt;
                }

            }
        }
        else {    //C연산

            for (int x = 0; x <= X; x++) {

                memset(num, 0, sizeof(num));
                for (int y = 0; y <= Y; y++) {
                    num[map[y][x]]++;
                    map[y][x] = 0;
                }

                vector<str> vec;
                for (int i = 1; i <= N; i++) {
                    if (num[i]) {
                        vec.push_back(str(i, num[i]));
                    }
                }

                sort(vec.begin(), vec.end());
                for (int i = 0, k = 0; i < vec.size(); i++, k += 2) {
                    map[k][x] = vec[i].value;
                    map[k + 1][x] = vec[i].cnt;
                }

            }
        }


        //y,x길이 새롭게
        int ny = 0;
        int nx = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j]) {
                    ny = max(ny, i);
                    nx = max(nx, j);
                }
            }
        }

        Y = ny;
        X = nx;
        ans++;
    }

    cout << ans << endl;

    return 0;
}

