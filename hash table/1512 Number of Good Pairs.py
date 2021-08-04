# 1512. Number of Good Pairs
'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''
# in this problem we use have to return the number of good pairs i.e. value of two elements in the array is same and the element appearing first 
# has index lower than the one appearing later , but it would be quite obvious 
# combinations method, takes two arguments(list,no. of elements to be put together)
# used to make pairs in this casse
import itertools
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i=0
        for a,b in itertools.combinations(nums,2):
            if a==b:
                i=i+1
        return i
       
# we only create a variable which is updated when any two elements are equal in the same list, therefore in the end of the for loop 
# this variable returns the number of good pairs
