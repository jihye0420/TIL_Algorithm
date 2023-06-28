#include <iostream>

#include <queue>

using namespace std;



const int MAX = 100000 + 1;



int N, T;

int A[MAX];

int copyA[MAX];

int result[MAX];



bool possible(int diff)

{

    for (int i = 0; i < N; i++)

        copyA[i] = A[i];



    int cnt = 0;

    //������ ������ üũ

    for (int i = 0; i < N - 1; i++)

        if (copyA[i + 1] - copyA[i] > diff)

        {

            cnt += copyA[i + 1] - (copyA[i] + diff);

            copyA[i + 1] = copyA[i] + diff;

        }

    //������ ���� üũ

    for (int i = N - 1; i > 0; i--)

        if (copyA[i - 1] - copyA[i] > diff)

        {

            cnt += copyA[i - 1] - (copyA[i] + diff);

            copyA[i - 1] = copyA[i] + diff;

        }



    //���� Ƚ���� T �����ΰ� üũ

    if (cnt <= T)

        return true;

    return false;

}



int main(void)

{

    ios_base::sync_with_stdio(0);

    cin.tie(0);

    cin >> N >> T;



    for (int i = 0; i < N; i++)

        cin >> A[i];



    int low = 0, high = MAX;

    int minDiff = MAX; //�ּ� ��

    while (low <= high)

    {

        int mid = (low + high) / 2;

        if (possible(mid))

        {

            for (int i = 0; i < N; i++)

                result[i] = copyA[i];

            high = mid - 1;

        }

        else

            low = mid + 1;

    }

    for (int i = 0; i < N; i++)

        cout << result[i] << " ";

    cout << "\n";

    return 0;

}