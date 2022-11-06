#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

vector<int> works;

int minusMax(int n){
    int mxN = works[0];
    int cnt = 0;
    
    if(mxN == 0) return 0;
    
    for(int i=0; i<works.size(); i++){        
        if(cnt >= n) return cnt;
        
        if(works[i] == mxN){
            if(works[i] > 0){
                works[i] -= 1;
                cnt += 1;
            }
        }
        
        else return cnt;
    }
    
    return cnt;
}

long long solution(int n, vector<int> input_works) {
    long long answer = 0;
    works  = input_works;
    
    sort(works.begin(), works.end(), greater<int>());
    
    while(n > 0){
        int ret = minusMax(n);
        
        sort(works.begin(), works.end(), greater<int>());
        if(ret == 0) break;
        n -= ret;
    }
    
    for(int i=0; i<works.size(); i++){
        answer += (works[i]*works[i]);
    }
    
    return answer;
}