#include <string>
#include <vector>
#include <set>
using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    int answer = 0;
    set<string> unq;
    
    for(int i=0; i<s1.size(); i++){
        unq.insert(s1[i]);
    }
        
    for(int i=0; i<s2.size(); i++){
        unq.insert(s2[i]);
    }
    
    answer = s1.size() + s2.size() - unq.size();
    return answer;
}