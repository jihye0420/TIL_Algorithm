#include <iostream>
using namespace std;

int map[101][101];
long long visited[101][101];

int main() {
	int n;
	cin >> n;


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
		}
	}
	visited[0][0] = 1;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] == 0)
				continue;
			if (i + map[i][j] < n)
				visited[i + map[i][j]][j] += visited[i][j];
			if (j + map[i][j] < n)
				visited[i][j + map[i][j]] += visited[i][j];
		}
	}
	cout << visited[n - 1][n - 1] << endl;

	return 0;
}