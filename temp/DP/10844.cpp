//10844_���� ��� ��
#include <iostream>
#define mod 1000000000
using namespace std;

int DP[101][101];

int main() {
    int n;
    int i, j;
    long long sum = 0;

    for (i = 1; i <= 9; ++i) {        //1�� �� �ʱ�ȭ -> 2���� �������� ���� �� ����
        DP[1][i] = 1;
    }

    cin >> n;

    for (i = 2; i <= n; ++i) {
        for (j = 0; j <= 9; ++j) {
            if (j == 0) DP[i][j] = DP[i - 1][j + 1];            //1������ �� �� ����
            else if (j == 9) DP[i][j] = DP[i - 1][j - 1];        //8������ �� �� ����
            else DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % mod;    //���ʿ��� �� �� ����
        }
    }

    for (i = 0; i <= 9; ++i) sum += DP[n][i];            //�� ����� ��

    cout << sum % mod << endl;

    return 0;
}