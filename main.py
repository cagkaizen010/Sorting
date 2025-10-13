import algorithm as algo
import string_gen as gen

import time

# sample size k = 5
# n = 128, 256, ..., 4096



# Input: null
# Output: CSV file containing
#          x-val: lengths of n
#          y-val: average running time across k-samples of each n
def main():

    # Sample Size
    # Modify k to change the amount of samples for each n 
    k = 50 


    n_sizes = 6 

    alg = "merge"

    file_name = f"data/{alg}_{k}k_{n_sizes}n.txt"

    suffix_array = []    

    ## Begin heading of CSV file for each sort
    with open(file_name,'w') as file:
        file.write("n,time\n")

    
    for i in range(0, n_sizes):

        # Define/reset the time array
        time_array = []
        for k_i in range(0,k):
            # gen_string = "tgtgtgtgcaccg" # Test string from prompt

            # Define timer start
            start_time = time.perf_counter()
            # Generate a random string
            gen_string = gen.string_gen(2**(7 + i))

            # Construct its suffix array
            suffix_array = SUFFIXARRAY(alg, gen_string)

            # measure the execution time 
            end_time = time.perf_counter()

            # Append the elapsed time to the time array
            time_array.append(end_time-start_time)

            ## Uncomment to observe suffix_array output
            # print(suffix_array)


        # print(time_array) # Uncomment to check for inaccurate "0.0" values
        avg_run_time = sum(time_array)/k   
        
        with open(file_name,'a') as file:
            file.write(str(2**(7 + i)) + ", " + str(avg_run_time))
            file.write("\n")



def SUFFIXARRAY(choice, unsorted_string):
    if (choice == "insertion"): return algo.insertion_sort(unsorted_string)
    elif (choice == "merge"): return algo.merge_sort(unsorted_string)
    else: print("Invalid choice")

main()