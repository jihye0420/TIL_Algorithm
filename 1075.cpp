#include <iostream>

using namespace std;



int N, F;



int getLast2Digit()

{

    //100�� �ڸ� ����

    int start = (N / 100) * 100;



    int result;

    //������ �� �ڸ��� ��

    for (int i = start; i < (start + 100); i++)

        //���� ���� ������ �������� ������ ���ڸ��� ����

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

    //1�ڸ� ���ڶ�� 0�� ���δ�

    if (result >= 0 && result < 10)

        cout << "0";

    cout << result << endl;

    return 0;

}