class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


def invert_tree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def has_path_sum(root, target_sum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target_sum

    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))


def all_paths_sum(root, target_sum):
    def dfs(node, current_sum, path, result):
        if not node:
            return

        current_sum += node.val
        path.append(node.val)

        if not node.left and not node.right and current_sum == target_sum:
            result.append(path[:])

        dfs(node.left, current_sum, path, result)
        dfs(node.right, current_sum, path, result)
        path.pop()

    result = []
    dfs(root, 0, [], result)
    return result


def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


def max_path_sum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum

        if not node:
            return 0

        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        current_path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path_sum)

        return node.val + max(left_gain, right_gain)

    dfs(root)
    return max_sum


def serialize(root):
    def dfs(node):
        if not node:
            return ['null']

        return [str(node.val)] + dfs(node.left) + dfs(node.right)

    return ','.join(dfs(root))


def deserialize(data):
    def dfs(nodes):
        val = next(nodes)
        if val == 'null':
            return None

        node = TreeNode(int(val))
        node.left = dfs(nodes)
        node.right = dfs(nodes)
        return node

    return dfs(iter(data.split(',')))


def is_balanced(root):
    def dfs(node):
        if not node:
            return 0, True

        left_height, left_balanced = dfs(node.left)
        right_height, right_balanced = dfs(node.right)

        balanced = (left_balanced and right_balanced and
                   abs(left_height - right_height) <= 1)

        return 1 + max(left_height, right_height), balanced

    _, balanced = dfs(root)
    return balanced


def diameter_of_tree(root):
    max_diameter = 0

    def dfs(node):
        nonlocal max_diameter

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        max_diameter = max(max_diameter, left + right)

        return 1 + max(left, right)

    dfs(root)
    return max_diameter
