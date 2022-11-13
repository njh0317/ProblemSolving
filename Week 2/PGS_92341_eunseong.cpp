#include <string>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

map<string, vector<pair<string,string>> > book;
 
void split(string str){
    
    stringstream ss(str);
    string buffer;
    
    vector<string> result;
    
    while(getline(ss, buffer, ' ')){
        result.push_back(buffer);
    }
    
    string carN = result[1];
    
    if(result[2] == "IN")
        book[carN].push_back({result[0], "23:59"});
    
    else
        book[carN].back().second = result[0];
}

int calTime(string time1, string time2){
    int minT1 = stoi(time1.substr(0,2))*60 + stoi(time1.substr(3,5));
    int minT2 = stoi(time2.substr(0,2))*60 + stoi(time2.substr(3,5));
    
    return minT2-minT1;
}

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    
    for(int i=0; i<records.size(); i++){
        split(records[i]);
    }
    
    for(auto m : book){
        int totalTime = 0, totalFee = fees[1];
        
        for(int i=0; i<m.second.size(); i++){
            int timeM = calTime(m.second[i].first, m.second[i].second);
            totalTime += timeM;            
        }
        
        if(totalTime > fees[0]){
            totalFee += (totalTime-fees[0])/fees[2]*fees[3];
            if( (totalTime-fees[0])% fees[2] != 0) totalFee += fees[3];
        }
        
        answer.push_back(totalFee);
    }
    
    return answer;
}