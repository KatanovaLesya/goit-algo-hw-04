import timeit
import random

# Функція сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Тестові дані
sizes = [1000, 2000, 5000, 10000]
times_insertion = []
times_merge = []
times_timsort = []

for size in sizes:
    # Генерація масиву випадкових чисел
    random_array = [random.randint(1, 1000) for _ in range(size)]
    
    # Вимірювання часу для сортування вставками
    time_insertion = timeit.timeit('insertion_sort(arr[:])', globals=globals(), setup=f'arr={random_array}', number=1)
    times_insertion.append(time_insertion)
    
    # Вимірювання часу для сортування злиттям
    time_merge = timeit.timeit('merge_sort(arr[:])', globals=globals(), setup=f'arr={random_array}', number=1)
    times_merge.append(time_merge)
    
    # Вимірювання часу для вбудованого сортування Python (Timsort)
    time_timsort = timeit.timeit('sorted(arr)', globals=globals(), setup=f'arr={random_array}', number=1)
    times_timsort.append(time_timsort)

# Повернення зібраних даних
sizes, times_insertion, times_merge, times_timsort
