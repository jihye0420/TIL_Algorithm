#include <iostream>

using namespace std;



int N, F;



int getLast2Digit()

{

    //100의 자리 시작

    int start = (N / 100) * 100;



    int result;

    //마지막 두 자리만 비교

    for (int i = start; i < (start + 100); i++)

        //제일 먼저 나누어 떨어지는 마지막 두자리가 정답

        if (i % F == 0)

        {

            result = i % 100;

            break;

        }

    return result;

}



int main(void)

{

    cin >> N >> F;



    int result = getLast2Digit();

    //1자리 숫자라면 0을 붙인다

    if (result >= 0 && result < 10)

        cout << "0";

    cout << result << endl;

    return 0;

}