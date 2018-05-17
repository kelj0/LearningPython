#!/usr/bin/python3
#Given an array of ints, return True if 6 appears as either 
#the first or last element in the array.
#The array will be length 1 or more.
def first_last6(nums):
  a=len(nums)-1
  a=int(a)
  if nums[0]==6 or nums[a]==6:
    return True
  else:
    return False
print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))