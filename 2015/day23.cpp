#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <cmath>


void day23() {
    double a = 1;
    double b = 0;

    std::vector<std::tuple<std::string, char, std::string> > lines;

    std::ifstream file ("input.txt");
    std::string value;
    if (file.is_open())
    while (!file.eof()) {
        std::getline(file, value);
        std::string start;
        if ((start = value.substr(0, 3)) == "jmp")
            lines.push_back(std::tuple<std::string, char, std::string>(start, ' ', value.substr(4)));
        else if (start == "jie" || start == "jio")
            lines.push_back(std::tuple<std::string, char, std::string>(start, value.at(4), value.substr(7)));
        else
            lines.push_back(std::tuple<std::string, char, std::string>(start, value.at(4), ""));
    }

    for (int line = 0; line < lines.size(); ) {
        if (std::get<0>(lines[line]) == "hlf")
        {
            if (std::get<1>(lines[line]) == 'a') { a /= 2; }
            else { b /= 2; }
            line++;
        }
        else if (std::get<0>(lines[line]) == "tpl")
        {
            if (std::get<1>(lines[line]) == 'a') { a *= 3; }
            else { b *= 3; }
            line++;
        }
        else if (std::get<0>(lines[line]) == "inc") 
        {
            if (std::get<1>(lines[line]) == 'a') { a++; }
            else { b++; }
            line++;
        }
        else if (std::get<0>(lines[line]) == "jmp")
        {
            line += std::stoi(std::get<2>(lines[line]));
        }
        else if (std::get<0>(lines[line]) == "jio")
        {
            if (std::get<1>(lines[line]) == 'a') { 
                if (a != 1) {
                    line++;
                    continue;
                }
            }
            else { 
                if (b != 1) {
                    line++;
                    continue;
                }
                    
            }
            line += std::stoi(std::get<2>(lines[line]));
        }
        else if (std::get<0>(lines[line]) == "jie")
        {
            if (std::get<1>(lines[line]) == 'a') { 
                if (std::fmod(a, 2) != 0) {
                    line++;
                    continue;
                }    
            }
            else { 
                if (std::fmod(b, 2) != 0) {
                    line++;
                    continue;
                }    
            }
            line += std::stoi(std::get<2>(lines[line]));
        }
                if (a < 0)
        {
            std::cout << a;
            std::cout << b;
            std::cout << line;
            std::cout << std::get<0>(lines[line]) << std::get<1>(lines[line]) << std::get<2>(lines[line]);
            break;
        }
        
    }
    std::cout << b;
}
