from tree_node import TreeNode

# Linear Search
# Worst Case: O(N)


def linear_search(nums: list[int], target: int):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# Binary Search
# Worst Case: O(LogN)


def binary_search(nums: list[int], target: int):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Depth-First Search
# Time Complexity: 0(V+E)
# V -> Vertices
# E -> Edges


def DFS(node, target, visited_set):
    if node is None:
        return False

    if node.val == target:
        return True

    visited_set.add(node)

    for neighbor in node.get_neighbors():
        if neighbor not in visited_set:
            if DFS(neighbor, target, visited_set):
                return True
    return False


# Breadth-First Search
# Time Complexity O(V+E)
# V -> Vertices
# E -> Edges


def BFS(start_node, target):
    queue = []
    visited_set = set()

    queue.append(start_node)
    visited_set.add(start_node)

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node.val == target:
            return True

        for neighbor in current_node.get_neighbors():
            if neighbor not in visited_set:
                queue.append(neighbor)
                visited_set.add(neighbor)
    return False


def main():

    target = 23

    # Binary search requires a sorted array
    sorted_arr = [2, 4, 7, 10, 23, 34, 45, 55, 68, 77, 89, 91]
    b_result = binary_search(sorted_arr, target)
    print(b_result)

    # Linear search works on any array
    unsorted_arr = [34, 7, 23, 89, 4, 23, 12, 0, 77, 18]
    l_result = linear_search(unsorted_arr, target)
    print(l_result)

    # Building a simple binary tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    dfs_result = DFS(root, target=1, visited_set=set())
    print(dfs_result)

    bfs_result = BFS(root, target=4)
    print(bfs_result)


if __name__ == "__main__":
    main()
