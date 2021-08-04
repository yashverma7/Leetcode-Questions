## Decompress Run-Length Encoded List
'''
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

Example 2:

Input: nums = [1,1,2,3]
Output: [1,3,3]
 

Constraints:

2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
'''

# the problem here wants us to create a new list with freq and values given in the fashion as freq followed by its corresponding value
# so we simply create a new list to store all the new elementts generated after we are done running the for loop in the manner that 
# it only runs for even place elements and the odd place corresponding elements are multiplied according to the freq by using double [[]] 
# or else the values would be multipied and not the times we want element to be produced 
# finally the list with all the elements is returned with required freq and values
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decomp=[]
        for i in range(0, len(nums), 2):
            decomp += [nums[i+1]]*nums[i]
        return decomp
 
