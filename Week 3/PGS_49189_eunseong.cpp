#include <bits/stdc++.h>
using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    
    unordered_map<int,vector<int> > graph;
    vector<int> vis(n+1);
    vis[1] = 1;
    
    for(int i=0; i<edge.size(); i++){
        graph[edge[i][0]].push_back(edge[i][1]);
        graph[edge[i][1]].push_back(edge[i][0]);
    }
    
    queue<int> Q;
    Q.push(1);
    
    while(!Q.empty()){
        int cur = Q.front(); 
        Q.pop();
        
        for(int i=0; i<graph[cur].size(); i++){
            if(vis[graph[cur][i]] == 0){ 
                vis[graph[cur][i]] = vis[cur] + 1;
                Q.push(graph[cur][i]);
            }
        }
    }
    
    sort(vis.begin(), vis.end(), greater<int>());
    
    for(int i=0; i<=n; i++){
        if(vis[i] == vis[0]) answer++;
        if(vis[i] < vis[0]) break;
    }
    
    return answer;
}