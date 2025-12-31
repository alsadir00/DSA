# time complexity == o(n) and space is o(1)
def insertion_sort(array, type):
    if type == 'DESC':
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] < key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
    elif type == 'ASC':
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

    print(f'The List after sorted in {type} order is {array}!')



list_1 = [1,4,2,7,33,66,33,86,94,3,2,55,88]
insertion_sort(list_1, 'ASC')