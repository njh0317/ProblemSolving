class Solution {
    fun solution(enroll: Array<String>, referral: Array<String>, seller: Array<String>, amount: IntArray): IntArray {
        var answer = IntArray(enroll.size)
        
        val nameToValue = mutableMapOf<String, Pair<Int, Int>>().withDefault { Pair(-1, -1) }
        val valToName = mutableMapOf<Int, String>()
        
        enroll.forEachIndexed { index, s ->  
            valToName[index] = s
            val value = if(referral[index] == "-") {
                Pair(index, -1)
            }else Pair(index, nameToValue[referral[index]]!!.first)
            nameToValue[s] = value
        }
        seller.forEachIndexed { index, s ->
            var money = amount[index]*100
            var name = s
            while(true){
                val notMyMoney = money/10
                val value = nameToValue[name]!!
                answer[value.first!!]+=money-notMyMoney
                money = notMyMoney
                if(value.second!! == -1 || notMyMoney == 0) break
                // println("money from $name to ${valToName[value.second!!]!!} $notMyMoney")
                name = valToName[value.second!!]!!
            }     
        }
        
        
        return answer
    }
}