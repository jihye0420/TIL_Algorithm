#include <iostream>
using namespace std;

int main() {
	int L, A, B, C, D;
	int l, a, b;
	cin >> L >> A >> B >> C >> D;
	a = A / D;
	b = B / C;
	if (0 < A % D && A % D < D) {
		a++;
	}
	if (0 < B % C && B % C < C) {
		b++;
	}

	if (a > b) {
		l = L - a;
	}
	if (a < b) {
		l = L - b;
	}

	cout << l << endl;

	return 0;
}