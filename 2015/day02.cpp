#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

int day02() {
    int sum = 0;

    std::ifstream file ("input.txt");
    std::string value;
    if (file.is_open())
    while (!file.eof()) {
        std::getline(file, value);
        int lwh[3];
        for (int i = 0; i < 3; i++) {
            int pos = value.find("x");
            lwh[i] = std::stoi(value.substr(0, pos));
            value.erase(0, pos + 1);
        }
        sum += (2 * lwh[0] * lwh[1]) + (2 * lwh[1] * lwh[2]) + (2 * lwh[2] * lwh[0]);
        int sums[] = {lwh[0] * lwh[1], lwh[1] * lwh[2], lwh[2] * lwh[0]};
        sum += *std::min_element(sums, sums + sizeof(sums)/sizeof(sums[0]));
    }
    return sum;
}

int main() {
    int ans = day02();
    std::cout << ans;
}