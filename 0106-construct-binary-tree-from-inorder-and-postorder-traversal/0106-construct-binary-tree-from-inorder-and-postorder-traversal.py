# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode()
        # inorder = tree.left + tree.root + tree.right
        # postorder = tree.left + tree.right + tree.root
        def build_tree(cur_in, cur_post):
            if not cur_in:
                return None
            root =  cur_post[-1] 
            cur = TreeNode()
            cur.val = root
            mid = cur_in.index(root)
            
            cnt_left = mid
            left_post = cur_post[:mid]
            right_post = cur_post[mid: -1]
                    
            cur.left = build_tree(cur_in[:mid], left_post)
            cur.right = build_tree(cur_in[mid + 1:], right_post)
            return cur
            
        head = build_tree(inorder, postorder)
        return head
        
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        val = postorder[-1]
        mid = inorder.index(val)
        tree = TreeNode(val)
        tree.left = self.buildTree(inorder[:-1], postorder[:-1])
        tree.right = self.buildTree(inorder[])
            
"""