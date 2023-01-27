#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

int main() {
	int number;
	cin >> number;
	string word;
	queue<int> q;
	for (int i = 0; i < number; i++) {
		cin >> word;
		if (word == "push") {
			int x;
			cin >> x;
			q.push(x);
			//cout << x << endl;
		}
		else if (word == "pop") {
			if (q.size()==0) {
				cout << -1 << endl;
			}
			else {
				cout << q.front() << endl;
				q.pop();
			}
		}
		else if (word == "size") {
			cout << q.size() << endl;
		}
		else if (word == "empty") {
			if (q.empty()) {
				cout << 1 << endl;
			}
			else {
				cout << 0 << endl;
			}
		}
		else if (word == "front") {
			if (q.empty()) {
				cout << -1 << endl;
			}
			cout << q.front() << endl;
		}
		else if (word == "back") {
			if (q.empty()) {
				cout << -1 << endl;
			}
			cout << q.back() << endl;
		}
	}
	return 0;
}