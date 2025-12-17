import random
import timeit

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def run_sort(sort_func, data):
    sort_func(data)

def generate_data(n, data_type):
    if data_type == "random":
        return [random.randint(0, 10_000) for _ in range(n)]
    
    if data_type == "sorted":
        return list(range(n))
    
    if data_type == "reversed":
        return list(range(n, 0, -1))
    
    if data_type == "nearly_sorted":
        arr = list(range(n))
        swaps = max(1, n // 20)
        for _ in range(swaps):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    return []

def measure_time(sort_func, data, repeats=3, number=1):
    times = timeit.repeat(
        stmt="run_sort(sort_func, data)",
        repeat=repeats,
        number=number,
        globals={"run_sort": run_sort, "sort_func": sort_func, "data": data}
    )
    return min(times)

def main():
    random.seed(42)

    algorithms = [
        ("Insertion sort", insertion_sort),
        ("Merge sort", merge_sort),
        ("Timsort (sorted)", sorted),
    ]

    data_types = ["random", "sorted", "reversed", "nearly_sorted"]

    sizes = [200, 500, 1000, 2000]

    print("Порівняння алгоритмів сортування (timeit)\n")

    for n in sizes:
        print(f"--- Розмір списку: {n} ---")
        for dt in data_types:
            data = generate_data(n, dt)
            print(f"\nТип даних: {dt}")

            for name, func in algorithms:
                t = measure_time(func, data, repeats=3, number=1)
                print(f"{name:18} -> {t:.6f} сек")
            print("\n")

if __name__ == "__main__":
    main()
