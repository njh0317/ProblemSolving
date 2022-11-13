class Solution {
    val maxTime = 60*23+59
    
    fun calMoney(t: Int, fees: IntArray):Int {
        var money = fees[1]
        var originTime = t
        originTime-=fees[0]
        if(originTime>0){
            var leftTime = if(originTime%fees[2] == 0) originTime/fees[2] else originTime/fees[2]+1
            money += fees[3]*leftTime
        }
        return money
    }
    fun solution(fees: IntArray, records: Array<String>): IntArray {
        var parking = mutableMapOf<String, Int>()
        var totalTime = mutableMapOf<String, Int>()
        records.forEach{ record ->
            val (time, carNum, info) = record.split(" ")
            val (h, m) = time.split(":").map{it.toInt()}
            if(info == "IN"){
                parking.put(carNum, h*60+m)
            }else {
                val inTime = parking[carNum]!!.toInt()
                parking.remove(carNum)
                val outTime = h*60+m
                totalTime[carNum]=totalTime.getOrDefault(carNum,0)+(outTime - inTime)
            }
        }
        parking.forEach{ key, value ->
            totalTime[key] = totalTime.getOrDefault(key,0)+(maxTime - value)
        }
        
        var answer = IntArray(totalTime.size)
        var index = 0
        val sortedTime = totalTime.toSortedMap(compareBy{it})
        sortedTime.forEach{ key, value ->
            answer[index++] = calMoney(value, fees)
        }
        return answer
    }
    fun addElement(arr: IntArray, element: Int): IntArray {
        val mutableArray = arr.toMutableList()
        mutableArray.add(element)
    return mutableArray.toIntArray()
}

}