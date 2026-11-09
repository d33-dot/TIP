#include <iostream>
// задача 1
int main() {
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i + j < n - 1)       std::cout << 0;
            else if (i + j == n - 1) std::cout << 1;
            else                     std::cout << 2;

            if (j < n - 1) std::cout << " ";
        }
        std::cout << "\n";
    }
    return 0;
}

//задача 1.2
#include <iostream>

void printRow(int i, int j, int n) {
    if (j == n) return;

    if (i + j < n - 1) {
        std::cout << 0;
    } else if (i + j == n - 1) {
        std::cout << 1;
    } else {
        std::cout << 2;
    }

    if (j < n - 1) {
        std::cout << " ";
    }

    printRow(i, j + 1, n);
}

void drawWall(int i, int n) {
    if (i == n) return;

    printRow(i, 0, n);
    std::cout << "\n";
    
    drawWall(i + 1, n);
}

int main() {
    int n;
    if (std::cin >> n) {
        drawWall(0, n);
    }
    return 0;
}



// задача 2
int main() {
    int n, m, w;
    std::cin >> n >> m >> w;

    int field[35][35] = {0}; // Создаем и сразу зануляем массив

    for (int k = 0; k < w; k++) {
        int r, c;
        std::cin >> r >> c;
        field[r - 1][c - 1] = -1; // Отмечаем гриб как -1
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (field[i][j] != -1) {
                int count = 0;
                // Проверяем 8 клеток вокруг
                for (int di = -1; di <= 1; di++) {
                    for (int dj = -1; dj <= 1; dj++) {
                        int ni = i + di;
                        int nj = j + dj;
                        if (ni >= 0 && ni < n && nj >= 0 && nj < m && field[ni][nj] == -1) {
                            count++;
                        }
                    }
                }
                field[i][j] = count;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (field[i][j] == -1) std::cout << "*";
            else std::cout << field[i][j];
        }
        std::cout << "\n";
    }
    return 0;
}


//задача 3
#include <iostream>
#include <string>

int main() {
    std::string s;
    int n;
    std::cin >> s >> n;

    for (int step = 1; step < n; step++) {
        std::string next_s = "";
        int i = 0;

        while (i < s.length()) {
            int count = 1;
            while (i + 1 < s.length() && s[i] == s[i + 1]) {
                count++;
                i++;
            }
            next_s += (count + '0'); // Превращаем цифру в символ
            next_s += s[i];
            i++;
        }
        s = next_s;
    }

    std::cout << s << "\n";
    return 0;
}
