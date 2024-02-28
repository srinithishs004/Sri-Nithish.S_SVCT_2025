'''
ANAGRAM
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    s1, s2 = s[:mid], s[mid:]
    
    # Count the occurrences of each character in both halves
    count_s1 = [0] * 26
    count_s2 = [0] * 26
    
    for char in s1:
        count_s1[ord(char) - ord('a')] += 1

    for char in s2:
        count_s2[ord(char) - ord('a')] += 1

    # Calculate the changes needed to make s1 an anagram of s2
    changes = 0
    for i in range(26):
        changes += abs(count_s1[i] - count_s2[i])

    return changes // 2

# Sample Input
print(anagram("aaabbb"))  
print(anagram("ab"))     
print(anagram("abc"))     
print(anagram("mnop"))    
print(anagram("xyyx"))     
print(anagram("xaxbbbxx"))
