#include <string>
#include <vector>
using namespace std;

vector<int> del;

void check_val(int flag, vector<int>& a){
    int start = 0, end = a.size()-1;
    
    if(flag == -1){
        start = end;
        end = 0;
    }
    
    int check = a[start];
    int idx = start + flag;
    while(1){
        if(check > a[idx]){
            check = a[idx];
            del[idx] = 0;
       }
        if(idx == end) break;
        idx += flag;
    }
}


int solution(vector<int> a) {
    int answer = 0;
    
    del.assign(a.size(), 1);
    del[0] = del[a.size()-1] = 0;
    
    check_val( 1, a);
    check_val(-1, a);
    
    for(int i=0; i<del.size(); i++){
        if(del[i] == 0)
            answer++;
    }
    
    return answer;
}