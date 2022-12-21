data class Skill(var type: Int, var r1: Int, var c1: Int, var r2: Int, var c2: Int, var degree: Int)
class Solution {
    fun solution(board: Array<IntArray>, skill: Array<IntArray>): Int {
        val N = board.size
        val M = board[0].size
        var sumBoard = Array(N + 1){ IntArray(M + 1) }
        skill.forEach { it ->
            val type = if(it[0] == 1) -1 else 1
            val r1 = it[1]
            val c1 = it[2]
            val r2 = it[3]
            val c2 = it[4] 
            val degree = it[5] * type
            
            sumBoard[r1][c1] += degree
            sumBoard[r2+1][c2+1] += degree
            sumBoard[r1][c2+1] -= degree
            sumBoard[r2+1][c1] -= degree
        }

        for(i in 1 .. N){
            for(j in 0 .. M){
                sumBoard[i][j] += sumBoard[i-1][j]
            }
        }

        for(j in 1 .. M){
            for(i in 0 .. N){
                sumBoard[i][j] += sumBoard[i][j-1]
            }
        }
        var answer = 0
        for(i in 0 until N) {
            for (j in 0 until M){
                if(board[i][j] + sumBoard[i][j]>0) answer+=1
            }
        }
        return answer
    }
}
fun main(){
    val test = Solution()
    val board = arrayOf(intArrayOf(1, 2, 3), intArrayOf(4, 5, 6), intArrayOf(7, 8, 9))
    val skill = arrayOf(intArrayOf(1,1,1,2,2,4), intArrayOf(1,0,0,1,1,2), intArrayOf(2,2,0,2,0,100))
    print(test.solution(board, skill))
}