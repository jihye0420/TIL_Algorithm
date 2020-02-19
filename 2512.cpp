#include <iostream>

#include <vector>

#include <algorithm>

using namespace std;



vector<int> v;



long long calc(int num)

{

    long long result = 0;

    for (int i = 0; i < v.size(); i++)

        result += min(v[i], num);



    return result;

}



int main(void)

{

    ios_base::sync_with_stdio(0);

    cin.tie(0);

    int N;

    cin >> N;



    vector<int> v(N);

    int maxBudget = 0;

    for (int i = 0; i < N; i++)

    {

        cin >> v[i];

        maxBudget = max(maxBudget, v[i]);

    }



    int M;

    cin >> M;



    int low = 0, high = maxBudget;

    int result;

    while (low <= high)

    {

        int mid = (low + high) / 2;

        long long sum = 0;

        for (int i = 0; i < N; i++)

            sum += min(v[i], mid);

        if (sum <= M)

        {

            result = mid;

            low = mid + 1;

        }

        else

            high = mid - 1;

    }

    cout << result << "\n";

    return 0;

}