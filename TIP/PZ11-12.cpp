#include <bits/stdc++.h>
using namespace std;

// ZADANIE 1
// int main() {
//     int n, m;
//     cin >> n >> m;
//     vector<vector<long long>> a(n, vector<long long>(m));
//     for (int i = 0; i < n; i++)
//         for (int j = 0; j < m; j++)
//             cin >> a[i][j];

//     vector<vector<long long>> dp(n, vector<long long>(m));
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < m; j++) {
//             if (i == 0 && j == 0) {
//                 dp[i][j] = a[i][j];
//             } else {
//                 long long best = LLONG_MIN;
//                 if (i > 0) best = max(best, dp[i - 1][j]);
//                 if (j > 0) best = max(best, dp[i][j - 1]);
//                 dp[i][j] = a[i][j] + best;
//             }
//         }
//     }

//     vector<pair<int, int>> path;
//     int i = n - 1, j = m - 1;

//     while (true) {
//         path.push_back({i, j});
//         if (i == 0 && j == 0) break;

//         if (i > 0 && (j == 0 || dp[i - 1][j] >= dp[i][j - 1]))
//             i--;
//         else
//             j--;
//     }

//     reverse(path.begin(), path.end());
//     for (auto [x, y] : path)
//         cout << x << " " << y << "\n";
// }

// ZADANIE 2
// int main() {
//     int n, d;
//     cin >> n >> d;
//     vector<int> a(n);
//     for (int &x : a) cin >> x;

//     sort(a.begin(), a.end());

//     int l = 0, r = a.back() - a.front();

//     while (l < r) {
//         int mid = (l + r) / 2;

//         int days = 1;
//         int start = a[0];

//         for (int i = 1; i < n; i++) {
//             if (a[i] - start > mid) {
//                 days++;
//                 start = a[i];
//             }
//         }

//         if (days <= d) r = mid;
//         else l = mid + 1;
//     }

//     cout << l;
// }

// ZADANIE 3
// int main() {
//     int n, k, l;
//     cin >> n >> k >> l;

//     vector<int> a(n);
//     for (int &x : a) cin >> x;

//     sort(a.rbegin(), a.rend());

//     long long ans = 0;
//     int taken = 0;

//     for (int i = 0; i < n && taken < k; ) {
//         int j = i;
//         while (j < n && a[j] == a[i]) j++;

//         int can = min(l, min(j - i, k - taken));
//         ans += 1LL * can * a[i];
//         taken += can;

//         i = j;
//     }

//     cout << ans;
// }

// ZADANIE 1 PZ-12
// int n, m, ans = -1;
// vector<string> g;
// vector<vector<int>> used;

// void dfs(int x, int y, int cnt) {
//     if (x < 0 || y < 0 || x >= n || y >= m) return;
//     if (g[x][y] == '1' || used[x][y]) return;

//     used[x][y] = 1;

//     if (g[x][y] == 'P') cnt++;

//     if (g[x][y] == 'E') {
//         ans = max(ans, cnt);
//         used[x][y] = 0;
//         return;
//     }

//     dfs(x + 1, y, cnt);
//     dfs(x - 1, y, cnt);
//     dfs(x, y + 1, cnt);
//     dfs(x, y - 1, cnt);

//     used[x][y] = 0;
// }

// int main() {
//     cin >> n >> m;
//     g.resize(n);
//     for (int i = 0; i < n; i++) cin >> g[i];

//     used.assign(n, vector<int>(m, 0));
//     dfs(0, 0, 0);

//     cout << max(ans, 0);
// }