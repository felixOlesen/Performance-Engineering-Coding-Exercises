# Bubble Sort
# Best Case: O(N)
# Worst Case: O(N^2)
# Average Case: O(N^2)


def bubble_sort(nums: list[int]):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums


# Insertion Sort
# Best Case: O(N)
# Worst Case: O(N^2)
# Average Case: O(N^2)


def insertion_sort(nums: list[int]):
    n = len(nums)
    for i in range(n):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key
    return nums


# Merge Sort
# Best Case: O(NLogN)
# Worst Case: O(NLogN)
# Average Case: O(NLogN)


def merge_sort(nums: list[int]):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[0:mid]
    right = nums[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if len(left) > 0:
        result.extend(left)
    elif len(right) > 0:
        result.extend(right)
    return result


# Quick Sort
# Best Case: O(NLogN)
# Worst Case: O(N^2)
# Average Case: O(NLogN)


def quick_sort(nums: list[int], low, high):
    if low < high:
        pivot_index = partition(nums, low, high)

        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)

    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
    temp = nums[i + 1]
    nums[i + 1] = nums[high]
    nums[high] = temp

    return i + 1


def main():
    # A simple unsorted array with duplicates and negative values
    b_result = bubble_sort([34, -7, 23, 89, 4, 23, -12, 0, 77, 18])
    print(b_result)

    i_result = insertion_sort([34, -7, 23, 89, 4, 23, -12, 0, 77, 18])
    print(i_result)

    m_result = merge_sort([34, -7, 23, 89, 4, 23, -12, 0, 77, 18])
    print(m_result)

    q_result = quick_sort([34, -7, 23, 89, 4, 23, -12, 0, 77, 18], low=0, high=9)
    print(q_result)


if __name__ == "__main__":
    main()
