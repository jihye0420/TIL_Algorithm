//10844_쉬운 계단 수
#include <iostream>
#define mod 1000000000
using namespace std;

int DP[101][101];

int main() {
    int n;
    int i, j;
    long long sum = 0;

    for (i = 1; i <= 9; ++i) {        //1일 때 초기화 -> 2부터 동적으로 구할 수 있음
        DP[1][i] = 1;
    }

    cin >> n;

    for (i = 2; i <= n; ++i) {
        for (j = 0; j <= 9; ++j) {
            if (j == 0) DP[i][j] = DP[i - 1][j + 1];            //1에서만 올 수 있음
            else if (j == 9) DP[i][j] = DP[i - 1][j - 1];        //8에서만 올 수 있음
            else DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % mod;    //양쪽에서 올 수 있음
        }
    }

    for (i = 0; i <= 9; ++i) sum += DP[n][i];            //총 경우의 수

    cout << sum % mod << endl;

    return 0;
}