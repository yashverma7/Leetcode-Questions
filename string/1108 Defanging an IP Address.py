# 1108. Defanging an IP Address
'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        jo=[]
        jo=address.replace(".","[.]")
        return jo
     
# the problem here is simple we have to replace "." with "[.]" 
# first a new list is created and elements from original list are modified acc to the problem statement 
# can be easily done by using replace method and finally return the new list
