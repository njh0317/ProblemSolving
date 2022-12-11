import kotlin.math.*
class Solution {
    fun solution(jobs: Array<IntArray>): Int {
        var answer = 0
        jobs.sortBy{it[1]}
        var list = jobs.toMutableList()
        var endTime = 0
        
        while(list.size>0){
            var flag = false
            var minStartTime = list[0][0]
            for(i in 0..list.size-1){
                if(list[i][0]<=endTime){
                    endTime += list[i][1]
                    answer+=(endTime-list[i][0])
                    list.removeAt(i)
                    flag = true
                    break
                }
                minStartTime = min(minStartTime, list[i][0])
            }
            if(!flag && list.size!=0){
                endTime = minStartTime
            }  
        }
        
        return answer/jobs.size
    }
}