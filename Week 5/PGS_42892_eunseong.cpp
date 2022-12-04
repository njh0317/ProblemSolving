#include <string>
#include <vector>
#include <algorithm>
using namespace std;
 
struct Node{
    int idx, x, y;
    Node *Left;
    Node *Right;
};
 
bool cmp(Node a, Node b){

    if(a.y == b.y){
        if(a.x < b.x){
            return true;
        }
        return false;
    }

    return (a.y > b.y);
}
 
void Make_BT(Node *Root, Node* Child){
    
    if (Root->x > Child->x){
        if (Root->Left == NULL){
            Root->Left = Child;
            return;
        }
        Make_BT(Root->Left, Child);
    }

    else{
        if (Root->Right == NULL){
            Root->Right = Child;
            return;
        }
        Make_BT(Root->Right, Child);
    }
}
 
void PreOrder(Node *Root, vector<int> &answer){
    if (Root == NULL) return;
    answer.push_back(Root->idx);
    PreOrder(Root->Left, answer);
    PreOrder(Root->Right, answer);
}
 
void PostOrder(Node *Root, vector<int> &answer){
    if (Root == NULL) return;
    PostOrder(Root->Left, answer);
    PostOrder(Root->Right, answer);
    answer.push_back(Root->idx);
}
 
vector<vector<int>> solution(vector<vector<int>> nodeinfo){
    vector<vector<int>> answer;
    vector<Node> Tree;

    for (int i = 0; i < nodeinfo.size(); i++){
        int x = nodeinfo[i][0];
        int y = nodeinfo[i][1];
        int idx = i + 1;
        Tree.push_back({ idx, x, y, NULL, NULL });
    }
    sort(Tree.begin(), Tree.end(), cmp);
    
    Node *Root = &Tree[0];
    
    for (int i = 1; i < Tree.size(); i++) 
        Make_BT(Root, &Tree[i]);
    
    vector<int> Pre_V; 
    PreOrder(Root, Pre_V);
    
    vector<int> Post_V;    
    PostOrder(Root, Post_V);
    
    answer.push_back(Pre_V);
    answer.push_back(Post_V);
    
    return answer;
}
