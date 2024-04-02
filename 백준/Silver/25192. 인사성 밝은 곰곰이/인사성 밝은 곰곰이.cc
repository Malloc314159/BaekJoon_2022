#include <iostream>
#include <set>

using namespace std;

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n, sum = 0;
    set<string> ppl;
    cin >> n;
    for (int i = 0;i < n;i++) {
        string tmp;
        cin >> tmp;
        if (tmp == "ENTER") {
            ppl.clear();
        }
        else if (!ppl.count(tmp)) {
            sum++;
            ppl.insert(tmp);
        }
    }
    cout << sum;
}
