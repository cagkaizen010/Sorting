   
#   Group 1: Insertion Sort 
#   Group 2: Merge Sort
def insertion_sort(input_string):
    print("Performing insertion sort...")

    string_arr = []
    original_arr = []

    for i in range(len(input_string)):
        string_arr.append(input_string[i:len(input_string)])

    original_arr = string_arr.copy()

    for i in range(len(string_arr)-1):
        for j in range(i, -1, -1):
            if(string_arr[j+1] < string_arr[j]):
                temp_str = string_arr[j+1]
                string_arr[j+1] = string_arr[j]
                string_arr[j] = temp_str


    for i in string_arr:
        print(str(original_arr.index(i))+ ": " + i )

def merge_sort(input_string):
    print("Performing merge sort...")
    string_arr = []
    original_arr = []

    for i in range(len(input_string)):
        string_arr.append(input_string[i:len(input_string)])

    original_arr = string_arr.copy()
    print(string_arr)

    sorted_arr = divide_half(string_arr)

    for i in sorted_arr:
        print(str(original_arr.index(i))+ ": " + i )
    

def sort(left, right):
    merged_array = []
    i1 = 0
    i2 = 0

    for i in range(len(left)+len(right)):
        if i2 == len(right) or (i1 < len(left) and left[i1] < right[i2]):
            merged_array.append(left[i1])
            i1 += 1
        else:
            merged_array.append(right[i2])
            i2 += 1

    return merged_array

def divide_half(string_arr):
    if len(string_arr) <= 1:
        return string_arr
    left_half = string_arr[len(string_arr) // 2:]
    right_half = string_arr[:len(string_arr) // 2]

    left_half = divide_half(left_half)
    right_half = divide_half(right_half)
    
    return sort(left_half, right_half)

