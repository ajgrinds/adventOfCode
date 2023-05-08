#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

int main() {
    int part1 = 0;
    int part2 = 0;

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
        part1 += (2 * lwh[0] * lwh[1]) + (2 * lwh[1] * lwh[2]) + (2 * lwh[2] * lwh[0]);
        int times[] = {lwh[0] * lwh[1], lwh[1] * lwh[2], lwh[2] * lwh[0]};
        part1 += *std::min_element(times, times + sizeof(times)/sizeof(times[0]));

        part2 += lwh[0] * lwh[1] * lwh[2];
        int sums[] = {lwh[0] + lwh[1], lwh[1] + lwh[2], lwh[2] + lwh[0]};
        part2 += *std::min_element(sums, sums + sizeof(sums)/sizeof(sums[0])) * 2;

    }
    std::cout << "Part 1: " << part1 << std::endl << "Part 2: " << part2;
}
