import java.util.LinkedList
class Solution {
    fun bfs(n: Int, graph : Array<ArrayList<Int>>):Int {
        val queue = LinkedList<Int>()
        val visited = arrayOfNulls<Int>(n+1)
        visited.fill(-1)
        var distance = 0
        var long_num = 0
        
        queue.add(1)
        visited[1] = 0
        
        while(queue.isNotEmpty()) {
            val vertex = queue.poll()
            val length = visited[vertex]
            graph[vertex].forEach { it ->
                if(visited[it] == -1){
                    queue.add(it)
                    visited[it] = length!! + 1
                    if(length + 1 > distance){
                        distance = length!! + 1
                        long_num = 1
                    } else if(length!! + 1 == distance){
                        long_num += 1
                    }
                }
            }
        }
        return long_num
    }
    fun solution(n: Int, edge: Array<IntArray>): Int {
        val graph = Array<ArrayList<Int>>(n+1) { ArrayList() }
        edge.forEach { it ->
            graph[it[0]].add(it[1])
            graph[it[1]].add(it[0])
        }
        val answer = bfs(n, graph)
        return answer
    }
}