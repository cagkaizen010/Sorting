import time
import timeit

#   Group 1: Insertion Sort 
#   Group 2: Merge Sort
def insertion_sort(input_string):

    suffix_arr =[]

    string_arr = []
    original_arr = []

    for i in range(len(input_string)):
        string_arr.append(input_string[i:len(input_string)])

    original_arr = string_arr.copy()    # Copy original array to preserve index of starting positions

    for i in range(len(string_arr)-1):
        for j in range(i, -1, -1):
            if(string_arr[j+1] < string_arr[j]):
                temp_str = string_arr[j+1]
                string_arr[j+1] = string_arr[j]
                string_arr[j] = temp_str

    for i in string_arr:
        
        suffix_arr.append(original_arr.index(i))

    # print(suffix_arr)
    return suffix_arr



def merge_sort(input_string):

    suffix_arr = []
    string_arr = []
    original_arr = []

    for i in range(len(input_string)):
        string_arr.append(input_string[i:len(input_string)])

    original_arr = string_arr.copy()

    sorted_arr = merge_sort_recursive(string_arr)

    for i in sorted_arr:
        suffix_arr.append(original_arr.index(i))
    return suffix_arr
    

def merge_sort_recursive(string_arr):
    if len(string_arr) <= 1:
        return string_arr
    left_half = string_arr[len(string_arr) // 2:]
    right_half = string_arr[:len(string_arr) // 2]

    left_half = merge_sort_recursive(left_half)
    right_half = merge_sort_recursive(right_half)
    
    merged_array = []
    i1 = 0
    i2 = 0

    for i in range(len(left_half)+len(right_half)):
        if i2 == len(right_half) or (i1 < len(left_half) and left_half[i1] < right_half[i2]):
            merged_array.append(left_half[i1])
            i1 += 1
        else:
            merged_array.append(right_half[i2])
            i2 += 1
    
    return merged_array

