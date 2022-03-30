/*
#include <iostream>
#include <string>
#include <cstring>

using namespace std;
int n, num;
string order;
bool arr[21];

int main() {

	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n;

	
	while (n--)
	{
		cin >> order;

		if (order == "add")
		{
			cin >> num;
			arr[num] = true;
		}
		else if (order == "remove") {
			cin >> num;
			arr[num] = false;
		}
		else if (order == "check") {
			cin >> num;
			if (arr[num]) {
				cout << 1 << '\n';
			}
			else {
				cout << 0 << '\n';
			}
		}
		else if (order == "toggle") {
			cin >> num;
			arr[num] = !arr[num];
		}
		else if (order == "all") {
			memset(arr, true, sizeof(arr));
		}
		else if (order == "empty") {
			memset(arr, false, sizeof(arr));
		}
	}

	return 0;
}
*/