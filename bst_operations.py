class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return

        current = self.root
        while True:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    return
                current = current.right

    def search(self, val):
        current = self.root
        while current:
            if val == current.val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, val):
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node, val):
        if not node:
            return None

        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            min_node = self._find_min(node.right)
            node.val = min_node.val
            node.right = self._delete_recursive(node.right, min_node.val)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def find_kth_smallest(self, k):
        stack = []
        current = self.root
        count = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            count += 1

            if count == k:
                return current.val

            current = current.right

        return None

    def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            node = self.root

        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (self.is_valid_bst(node.left, min_val, node.val) and
                self.is_valid_bst(node.right, node.val, max_val))

    def lowest_common_ancestor(self, p, q):
        current = self.root

        while current:
            if p < current.val and q < current.val:
                current = current.left
            elif p > current.val and q > current.val:
                current = current.right
            else:
                return current.val

        return None
