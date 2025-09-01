def maxmin_select(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    else:
        mid = len(arr) // 2
        left_max, left_min = maxmin_select(arr[:mid])
        right_max, right_min = maxmin_select(arr[mid:])
        return max(left_max, right_max), min(left_min, right_min)

def main():
    arr = [12, 45, 7, 23, 56, 89, 34]
    max_element, min_element = maxmin_select(arr)
    print("Maior elemento:", max_element)
    print("Menor elemento:", min_element)

if __name__ == "__main__":
    main()