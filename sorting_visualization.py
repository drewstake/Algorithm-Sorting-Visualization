import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def merge_sort(arr, *args):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        yield from merge_sort(left_half)
        yield from merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        yield arr

def quick_sort(arr, low, high, *args):
    if low < high:
        pivot_index = partition(arr, low, high)
        yield from quick_sort(arr, low, pivot_index - 1)
        yield from quick_sort(arr, pivot_index + 1, high)
    yield arr

def partition(arr, low, high, *args):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right

def shell_sort(arr, *args):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            yield arr
        gap //= 2



def bubble_sort(arr, *args):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

def selection_sort(arr, *args):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

def heap_sort(arr, *args):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        yield arr


def insertion_sort(arr, *args):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

def counting_sort(arr, *args):
    n = len(arr)
    max_element = max(arr)
    count_array = [0] * (max_element + 1)

    for element in arr:
        count_array[element] += 1

    sorted_array = []
    for i in range(len(count_array)):
        sorted_array.extend([i] * count_array[i])
        yield sorted_array

def radix_sort(arr, *args):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        buckets = [list() for _ in range(10)]
        for i in arr:
            buckets[(i // exp) % 10].append(i)
        arr = [i for bucket in buckets for i in bucket]
        exp *= 10
        yield arr

def bucket_sort(arr, *args):
    n = len(arr)
    bucket_size = 10
    max_value = max(arr)
    min_value = min(arr)
    bucket_count = (max_value - min_value) // bucket_size + 1

    buckets = [[] for _ in range(bucket_count)]

    for i in range(n):
        buckets[(arr[i] - min_value) // bucket_size].append(arr[i])

    arr = []
    for i in range(bucket_count):
        buckets[i].sort()
        arr += buckets[i]
        yield arr

def cocktail_sort(arr, *args):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            yield arr

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            yield arr

        start += 1

def random_sort(arr, *args):
    n = len(arr)
    for i in range(n):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
        yield arr

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogosort(arr, *args):
    while not is_sorted(arr):
        random.shuffle(arr)
        yield arr



def visualize_sorting_algorithm(algorithm, arr, *args):
    fig, ax = plt.subplots()
    ax.set_title(algorithm.__name__)

    bar_rects = ax.bar(range(len(arr)), arr, align='edge')

    text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    iteration = [0]

    def update(arr, rects, iteration, text):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f'# of operations: {iteration[0]}')
        
    frames = (array_state for array_state in algorithm(arr, *args) if array_state != arr)
    anim = animation.FuncAnimation(fig, func=update, fargs=(bar_rects, iteration, text), frames=algorithm(arr, *args), interval=1, repeat=False)
    plt.show()


def main():
    while True:
        algorithms = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, shell_sort, heap_sort, counting_sort, radix_sort, bucket_sort, cocktail_sort, bogosort]
        array_size = 100
        arr = [random.randint(1, 100) for _ in range(array_size)]

        print("Choose a sorting algorithm:")
        for i, algorithm in enumerate(algorithms, start=1):
            print(f"{i}. {algorithm.__name__}")
        print(f"{len(algorithms) + 1}. Exit")

        choice = int(input("Enter the number of your choice: ")) - 1

        if choice == len(algorithms):
            print("Exiting the program.")
            break

        selected_algorithm = algorithms[choice]
        print(f"Visualizing {selected_algorithm.__name__}")
        visualize_sorting_algorithm(selected_algorithm, arr, 0, len(arr) - 1)

main()
