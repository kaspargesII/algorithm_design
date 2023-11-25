# Problem description: I have a set of positive integers 
#. Can you find two non-empty, distinct subsets with the same sum?

# Input structure: First line is the number of test cases, T. 
# T test cases follow, one per line. Test case begins with N, the number
# of numbers in the set.

# All numbers in the set are distinct.
# N is max 20. 

# My initial thought is that we can brute force this seeing as N is limited to 
# 20. 
# We check all possible sums iteratively; I thought sorting might be useful in finding sums faster. However given no 
# guarantees on the input I doubt it is worth it. 

# Actually I dont think it is quadratic or brute forceable. 


# Output:
#If there are two different subsets of 
# that have the same sum, then output these subsets, one per line. 
#Each line should contain the numbers in one subset, separated by spaces.

# input reading:
test_cases = int(input())
for test_case in range(test_cases):
    test_case_set = list(map(int,input().split()))
    for number in test_case_set:
        for second_number in test_case_set:
            if number != second_number:
                possible_sum = number + second_number