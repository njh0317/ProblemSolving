#include <vector>
#include <algorithm>

using namespace std;
   
long long solution(int n, vector<int> times) {
    long long answer = 0;
    
    sort(times.begin(), times.end());
    
    long long lo = 1;
    long long hi = times.back()* (long long)n;
    long long mid = 0;
    
    while(lo <= hi){
        
        mid = (lo+hi)/2;
        long long cnt = 0;
        
        for(int i=0; i<times.size(); i++){
            cnt += (mid/ times[i]);            
            if(cnt >= n) break;
        }
        
        if(cnt >= n){
            answer = mid;
            hi = mid-1;
        }
        else{
            lo = mid+1;
        }
    
    }
    
    return answer;
}