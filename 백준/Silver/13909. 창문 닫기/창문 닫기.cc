#include <iostream>
#include <cmath>

using namespace std;

int main() {
	long long int n, cnt=0;
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> n;

	for (int i = 1;i <= n;i++) {
		if (i * i > n) break;
		cnt++;
	}
	cout << cnt;
	return 0;
}