#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> answer;
vector<vector<string>> tic;

int vis[10001];
int flag = 1;

void dfs(int depth, string airport){
    
    if(depth == tic.size()){
        answer.push_back(airport);
        flag = 0;
        return ;
    }
    
    for(int i=0; i<tic.size(); i++){
        if(vis[i] == 0 && tic[i][0] == airport){
            vis[i] = 1;
            answer.push_back(airport);
        
            dfs(depth+1, tic[i][1]);
            
            if(flag){
                answer.pop_back();
                vis[i] = 0;
            }
        }
    }
}

vector<string> solution(vector<vector<string>> tickets) {
    tic = tickets;
    sort(tic.begin(), tic.end());
    
    dfs(0, "ICN");
    return answer;
}
