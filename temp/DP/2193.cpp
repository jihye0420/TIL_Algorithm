#include <vector>
#include <iostream>
using namespace std;
int dp[91];

int main(void) {


    int n;
    cin >> n;

    dp[1] = 1;      // ��ģ���� 0���� �������� �����Ƿ� 1��
    dp[2] = 1;
    // ����� ������ ���� �����ؼ� dp��ȸ
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    cout << dp[n] << "\n";

    return 0;
}