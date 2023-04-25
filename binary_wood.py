class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.answer = 0

    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.answer

    def helper(self, node: TreeNode) -> int:
        if node is None:
            return 0
        maxLeftPath = max(self.helper(node.left), 0)
        maxRightPath = max(self.helper(node.right), 0)
        self.answer = max(self.answer, maxLeftPath + maxRightPath + node.val)
        return max(maxLeftPath, maxRightPath) + node.val


# Создаем узлы дерева
node_1 = TreeNode(-10)
node_2 = TreeNode(9)
node_3 = TreeNode(20)
node_4 = TreeNode(-3)
node_5 = TreeNode(8)
node_6 = TreeNode(5)
node_7 = TreeNode(-4)
node_8 = TreeNode(-2)

# Строим связи между узлами
node_1.left = node_2
node_1.right = node_3
node_3.left = node_4
node_3.right = node_5
node_4.left = node_6
node_4.right = node_7
node_5.right = node_8

# Создаем объект класса Solution
s = Solution()

# Находим максимальную сумму пути
max_sum = s.maxPathSum(node_1)

# Выводим результат
print(max_sum)
