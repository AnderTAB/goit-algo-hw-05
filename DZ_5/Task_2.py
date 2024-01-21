def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    count = 0

    if upper_bound < x:
        return -1

    while low <= high:
        count += 1

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return mid

    # якщо елемент не знайдений
    return (count, upper_bound)


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
    x = 59

    result = binary_search(arr, x)

    if result != -1:
        print("Кількість ітерацій, індекс елемента", result)
    else:
        print("Element is not present in array")