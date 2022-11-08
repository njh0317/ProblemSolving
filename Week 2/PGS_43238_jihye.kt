class Solution {
    var person = 0
    fun checkPossibility(times: IntArray, time: Long):Boolean {
        var possibleNum = 0
        times.forEach { it ->
            possibleNum += (time/it).toInt()
            if(possibleNum >= person) return true
        }
        return false
    }
    
    fun solution(n: Int, times: IntArray): Long {
        person = n
        times.sort()
        var minTime = 1.toLong()
        var maxTime:Long = n*times[0].toLong()
        
        while(minTime < maxTime){
            var middleTime = (minTime+maxTime)/2
            if(checkPossibility(times, middleTime)){
                maxTime = middleTime
            }else {
                minTime = middleTime + 1
            }
        }
        var answer = maxTime
        return answer
    }
}