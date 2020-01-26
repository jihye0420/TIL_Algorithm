#include <vector>
#include <iostream>
using namespace std;
int dp[91];

int main(void) {


    int n;
    cin >> n;

    dp[1] = 1;      // 이친수는 0으로 시작하지 않으므로 1값
    dp[2] = 1;
    // 저장된 값으로 부터 시작해서 dp순회
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    cout << dp[n] << "\n";

    return 0;
}