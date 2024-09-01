def bubble_sort(arr: list[int]):
    """冒泡算法"""
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already sorted
        for j in range(n-i-1):
            # 当前元素大于下一个元素，交换它们的位置
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    arr = list(range(10))
    print(bubble_sort(arr))

# if __name__ == "__main__":
#     arr = [64, 34, 25, 12, 22, 11, 90]
#     print(bubble_sort(arr))
