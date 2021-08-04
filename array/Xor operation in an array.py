## XOR Operation in an Array
'''
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.

Example 2:

Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.

Example 3:

Input: n = 1, start = 7
Output: 7

Example 4:

Input: n = 10, start = 5
Output: 2
 

Constraints:

1 <= n <= 1000
0 <= start <= 1000
n == nums.length
'''
# in this problem first the list is generated according to the input by taking the start point and the number of elements 
# that will follow the pattern which in this case is a gap of 2 
# we have to apply bitwise XOR on all elements , it can be done through reduce and lambda methods,
# x,y are two demo consecutive elements and as we go through the list bitwise XOR is applied on every element through ^ operator 
# assigned by python itself and finally we can return the result
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]*1000
        for i in range(0,n):
            nums.append(start + 2*i)
        res=reduce(lambda x,y: x^y , nums)
        return res
# The reduce(fun,seq) function is used to apply a particular function passed in 
# its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.    
# this can also be used when solving the running sum problem 
