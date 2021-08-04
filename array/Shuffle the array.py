## Shuffle the Array
'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].


Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
'''
# in this problem , we need to add elements from second half of the list into a new list alternatively
# create 3 different lists , first two for handling the elements for first and second half and third for the final merger
# num1=nums[:length] copies the content of the first half of the list nums to num1 since lenght is equal to the half the length of nums
# arr1=nums[:x] everything before xth element is assigned to arr1 from nums 
# similarly for arr2=nums[x:] everything after xth element is assigned to arr2 from nums i
# so now we have two separate lists and now will run a for loop which adds elements one by one from these two lists into the third list and finally returns a 
# list with mixed elements
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num1=[]
        num2=[]
        num3=[]
        length=len(nums)//2
        num1=nums[:length]
        num2=nums[length:]
        for i in range(n):
            num3.append(num1[i])
            num3.append(num2[i])
            i+=1
        return num3    
    
        
        
