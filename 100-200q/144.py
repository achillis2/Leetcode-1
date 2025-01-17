'''
	Given a binary tree, return the preorder traversal of its nodes' values.

	Example:

	Input: [1,null,2,3]
	   1
		\
		 2
		/
	   3

	Output: [1,2,3]
	Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []

		stack, result = [root], []
		while stack:
			element = stack.pop()
			result.append(element.val)

			if element.right:
				stack.append(element.right)
			if element.left:
				stack.append(element.left)

		return result


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		result = []

		def recursive(root, result):
			if not root:
				return 
			result.append(root.val)
			recursive(root.left, result)
			recursive(root.right, result)

		recursive(root, result)
		return result

def get_test_case1():
	# test case 1
	root = TreeNode(1)
	node2 = TreeNode(2)
	node3 = TreeNode(3)
	node4 = TreeNode(4)
 
	root.right = node2
	node2.left = node3
	root.left = node4
 
	test_solution = Solution()
	return test_solution, root

sol, root = get_test_case1()

print(sol.preorderTraversal(root))