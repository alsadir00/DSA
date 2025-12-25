

def Selection_Sort(array, type):
    if type == 'DESC':
        for i in range(len(array)):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[min_index] < array[j]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]

    elif type == 'ASC':
        for i in range(len(array)):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[min_index] > array[j]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
            
    print(f'The List after sorted in {type} order is {array}!')



list_1 = [1,4,2,7,33,66,33,86,94,3,2,55,88]
Selection_Sort(list_1, 'ASC')