#!/usr/bin/python3


# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in
# the array, and it should return false if every element is distinct.
# Runtime 136 ms

def contains_duplicates(nums):    
    
    return(True if len(nums) < 2 else len(set(nums)) != len(nums))

if __name__=="__main__":

    # Test Cases:
    nums_1 = [1, 2 ,3 ,1]
    nums_2 = [3 ,1]
    nums_3 = [1]
    print(contains_duplicates(nums_1))
    print(contains_duplicates(nums_2))
    print(contains_duplicates(nums_3))