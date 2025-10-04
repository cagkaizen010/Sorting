import random
import string

# Input: Size n of the string
# Output: String of size n
def string_gen(main_n ):
    
    # Sample size

    content=""



    for x in range(0, main_n):
        content += random.choice(['a', 'c', 'g', 't'])
        
    return content
