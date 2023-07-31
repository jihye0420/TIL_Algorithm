#include <iostream>

#include <vector>

#include <string>

#include <algorithm>

using namespace std;



int main(void)

{

    ios_base::sync_with_stdio(0);

    cin.tie(0);

    int N, M;

    cin >> N >> M;



    vector<string> v(N + 1);

    for (int i = 1; i <= N; i++)

        cin >> v[i];



    //�̺� Ž���� ���� ������ ����

    vector<pair<string, int>> sortV(N);

    for (int i = 0; i < N; i++)

    {

        sortV[i].first = v[i + 1];

        sortV[i].second = i + 1;

    }



    sort(sortV.begin(), sortV.end());

    for (int i = 0; i < M; i++)

    {

        string s;

        cin >> s;



        //�ε����� �Էµ� ���

        if (s[0] >= '0' && s[0] <= '9')

        {

            int idx = 0;

            for (int j = 0; j < s.length(); j++)

            {

                idx += s[j] - '0';

                idx *= 10;

            }

            idx /= 10;

            cout << v[idx] << "\n";

        }

        //�̸��� �Էµ� ��� �̺� Ž���ϴ� ���

        else

        {

            int low = 0, high = N - 1;

            while (low <= high)

            {

                int mid = (low + high) / 2;

                //cout << low << " " << mid << " " << high << "\n";

                if (sortV[mid].first == s)

                {

                    cout << sortV[mid].second << "\n";

                    break;

                }

                else if (sortV[mid].first < s)

                    low = mid + 1;

                else

                    high = mid - 1;

            }

        }

    }

}