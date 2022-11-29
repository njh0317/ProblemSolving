class Solution {
    fun solution(a: IntArray): Int {
        var answer: Int = 0
        var arrayLength = a.size
        
        var minNum1 = 1000000000
        var minNum2 = 1000000000
        
        var booleanArray = Array(arrayLength){i -> false}
        for (i in 0 until arrayLength) {
            if(a[i]<minNum1) {
                minNum1 = a[i]
                if(!booleanArray[i]) {
                    answer+=1
                    booleanArray[i] = true
                }
            }
            
            if(a[arrayLength-i-1]<minNum2){
                minNum2 = a[arrayLength-i-1]
                if(!booleanArray[arrayLength-i-1]){
                    answer+=1
                    booleanArray[arrayLength-i-1] = true
                }
            }
        }
        return answer
    }
}