# https://leetcode.com/problems/print-binary-tree/
'''

Print a binary tree in an m x n 2D string array following these rules:

The row numbers m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exact middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.


Example 1:


Input: root = [1,2]
Output:
[["","1",""],
 ["2","",""]]

'''

'''
思路：
1. 计算depth层数(一个root为1层）
2. 每层2^(d-1) 个node
2. 数组的宽度为：2^d -1
'''
from treeNode import TreeNode;
class Solution:
    def printTree(self, root: TreeNode) :
        pass
