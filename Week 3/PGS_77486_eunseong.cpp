#include <bits/stdc++.h>
using namespace std;

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {   
    unordered_map<string, string> graph;
    unordered_map<string, int> total_profit;
    
    //Make graph
    for(int i=0; i<referral.size(); i++){
        if(referral[i] == "-")
            graph[enroll[i]] = "center";
        else
            graph[enroll[i]] = referral[i];
    }
    
    //Seller
    for(int i=0; i<seller.size(); i++){
        int profit = amount[i]*100;
        string cur = seller[i];
        
        while(cur != "center" && profit >= 1){            
            total_profit[cur] += (profit - profit/10);
            profit = profit/10;
            cur = graph[cur];
        }
        
        total_profit[cur] += profit;
    }
    
    vector<int> answer;
    
    for(int i=0; i<enroll.size(); i++){
        answer.push_back(total_profit[enroll[i]]);
    }
    
    return answer;
}