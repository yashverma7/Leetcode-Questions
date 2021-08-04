## Running Sum of 1d Array
'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''

# the idea here is to add up array elements as we go traversing through the list and keep updating the list accordingly.
# so the for loop runs through the list nums from first element till the complete length of nums list

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
# nums[i]=nums[i-1]+nums[i] in array [3,1,2,10,1] will start from nums[1]=nums[0]+nums[1] since first element will remain same in this problem as it doesn't have a predessor 
# so nums[1] will be 4 and then nums[2]=nums[1]+mums[2] 4+2=6 nums[2]=6 and so on nums[3]=16 and nums[4]=17
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        return nums
    
