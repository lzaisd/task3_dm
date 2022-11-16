def insertion_sort(array):
    count = 0
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 1 and array[j] > temp:
            count += 1
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    sort_arr = array
    sort_arr.append(count)
    return sort_arr


def shaker_sort(array):
    left = 0
    right = len(array) - 1
    count = 0
    while left <= right:
        for i in range(left, right, +1):
            if array[i] > array[i + 1]:
                count += 1
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
        right -= 1
        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                temp = array[i]
                array[i] = array[i - 1]
                array[i - 1] = temp
        left += 1
    sort_arr = array
    sort_arr.append(count)
    return sort_arr


fileInput = open('input.txt')
arr = []
line = fileInput.readline()
arr.extend([int(x) for x in line.split()])

# new_arr = insertion_sort(arr)
new_arr = shaker_sort(arr)

count_result = new_arr[len(new_arr) - 1]
del new_arr[len(new_arr) - 1]
sorted_arr = new_arr

fileOutput = open('output.txt', 'w')
for elem in sorted_arr:
    fileOutput.write(str(elem) + ' ')
fileOutput.write(" \n" + str(count_result))

fileOutput.close()
fileInput.close()
