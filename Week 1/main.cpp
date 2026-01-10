#include <iostream>
#include <string>
#include <fstream>
#include <regex>

using namespace std;

int CountMatches(string line) {

    regex words_regex("faust", regex_constants::icase);
    
    auto words_begin = sregex_iterator(line.begin(), line.end(), words_regex);
    auto words_end = sregex_iterator();

    return distance(words_begin, words_end);
}

void ReadFaust() {
    ifstream file("faust.txt");

    string line;
    int faustTotal = 0;
    if (file.is_open()) {
        int matchCount = 0;
        while (getline(file, line)) {
            matchCount = CountMatches(line);
            if(matchCount > 0) {
                faustTotal += matchCount;
            }
        }
    cout << "Total instances of 'Faust': " << faustTotal << endl;
    file.close();
    

    } else {
        cerr << "Unable to open file" << endl;
    }

}

int main() {
    ReadFaust();
    return 0;
}

