#include <iostream>
#include <string>
#include <fstream>
#include <set>

void day03() {
    std::pair<int, int>* starter = new std::pair<int, int>(0, 0);
    std::set<std::pair<int, int> > squares = {*starter};
    std::pair<int, int> santa = *starter;
    std::pair<int, int> robot_santa = *starter;
    
    std::ifstream file ("input.txt");
    char value;
    if (file.is_open())
    while (!file.eof()) {
        starter = *starter == santa ? &robot_santa : &santa;
        value = file.get();
        switch (value) {
            case '>':
                (*starter).first++;
                break;
            case '<':
                (*starter).first--;
                break;
            case '^':
                (*starter).second++;
                break;
            case 'v':
                (*starter).second--;
                break;
        }
        squares.insert(*starter);
    }
    std::cout << squares.size();
    
}
