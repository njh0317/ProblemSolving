#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;
struct cmp{
    bool operator()(vector<int> a, vector<int> b){
        return a[1] > b[1];
    }
};

int solution(vector<vector<int>> jobs) {
    int time = 0, idx = 0;
    int ans = 0;
    
    sort(jobs.begin(), jobs.end());
    priority_queue<vector<int>, vector<vector<int>>, cmp> pq;
    
    //cout << "start : " << jobs[0][0] << " " <<jobs[1][0] << "\n";
    while(idx < jobs.size() || !pq.empty()){
        
        while(jobs.size() > idx && time >= jobs[idx][0]){
            pq.push(jobs[idx]);
            idx++;
        }
        
        if(!pq.empty()){
            //cout << pq.top()[0] << " " << pq.top()[1] <<'\n';
            
            time += pq.top()[1];
            ans += (time - pq.top()[0]);
            pq.pop();
        }
        else{
            time = jobs[idx][0];
        }
    }
    // cout << time << '\n';
    return ans/jobs.size();
}