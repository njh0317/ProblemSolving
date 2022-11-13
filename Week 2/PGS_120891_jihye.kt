class Solution {
    fun solution(order: Int): Int {
        var answer: Int = 0
        var stringOrder = order.toString()
        for(i in 0..stringOrder.length-1){
            var num = Character.getNumericValue(stringOrder[i])
            if(num!=0 && num%3==0) answer+=1
        }
        return answer
    }
}