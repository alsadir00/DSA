
# time compexity == o(n) and space is o(1)
def Bubble_Sort(array, type):
    if type == 'DESC':
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
    elif type == 'ASC':
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

    print(f'The List after sorted in {type} order is {array}!')



list_1 = [1,4,2,7,33,66,33,86,94,3,2,55,88]
Bubble_Sort(list_1, 'ASC')