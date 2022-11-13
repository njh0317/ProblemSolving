class Solution {
    public int solution(int order) {
        int answer = 0;
        String str = Integer.toString(order);
        
        for(int i=0; i<str.length(); i++){
            if(str.charAt(i) != '0' && (str.charAt(i)-'0') %3 == 0) answer+=1;
        }
        
        return answer;
    }
}