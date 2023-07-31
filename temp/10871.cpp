#include <iostream>
using namespace std;

int main() {
	int n, p;
	int arr[100000];
	cin >> n >> p;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i < n; i++) {
		if (p > arr[i])
			cout << arr[i] << " ";
	}
	return 0;
}