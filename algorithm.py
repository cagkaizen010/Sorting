   
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
    sorted_array = []
    print("Input string: " + input_string)

