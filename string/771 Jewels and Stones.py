# 771. Jewels and Stones
'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.'''
# the problem here demands to check if the elements from first string are present in the second string 
# but strings' characters can't be compared character by character
# so we make two lists corresponding to these strings and run two loops simultaneously to check if the elements of the lists are same
# variable i is incremented at the event when two elements match
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        arrjewels=list(jewels)
        arrstones=list(stones)
        i=0
        for x, y in [(x,y) for x in arrjewels for y in arrstones]:
            if x==y:
                i+=1
        return i
