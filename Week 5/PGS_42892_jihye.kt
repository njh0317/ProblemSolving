import java.util.*
data class TreeNode<T>(var data: T, var index: T, var left: TreeNode<T>? = null, var right: TreeNode<T>? = null)

class BinaryTree {
    var root: TreeNode<Int>? = null
    
    fun insert(index: Int, x: Int){
        if(root == null){
            root = TreeNode(x, index)
        }else search(root!!, index, x)
    }
    
    private fun search(root: TreeNode<Int>, index: Int, x: Int){
        if(root.data > x){
            if(root.left == null){
                var leftNode = TreeNode(x, index)
                root.left = leftNode
            } else search(root.left!!, index, x)
        }else {
            if(root.right == null){
                var rightNode = TreeNode(x, index)
                root.right = rightNode
            } else search(root.right!!, index, x)
        }
    }
    
    fun preOrder(node: TreeNode<Int>):MutableList<Int> {
        var array = mutableListOf<Int>()
        array.add(node.index)
        if(node.left!=null) array+=preOrder(node.left!!)
        if(node.right!=null) array+=preOrder(node.right!!)
        return array
    }
    fun postOrder(root: TreeNode<Int>):MutableList<Int> {
        var array = mutableListOf<Int>()
        if(root.left!=null) array+=postOrder(root.left!!)
        if(root.right!=null) array+=postOrder(root.right!!)
        array.add(root.index)
        return array
    }
}
class Solution {
    fun solution(nodeinfo: Array<IntArray>): Array<IntArray> {
        var newnode = nodeinfo.sortedWith(compareBy({-it[1]},{it[0]}))
        val binaryTree = BinaryTree()
        
        newnode.forEach { it ->
            var index = nodeinfo.indexOf(it)+1
            binaryTree.insert(index, it[0])
        }
        var answer = arrayOf<IntArray>(binaryTree.preOrder(binaryTree.root!!).toIntArray(), binaryTree.postOrder(binaryTree.root!!).toIntArray())
        return answer
    }
}