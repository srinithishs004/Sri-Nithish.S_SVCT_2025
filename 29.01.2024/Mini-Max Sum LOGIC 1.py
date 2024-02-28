#!/bin/python3

import math
import os
'''
MINI-MAX SUM
'''
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    mini,maxi=0,0
    for i in range(0,len(arr)-1):
        mini+=arr[i]
        
    for i in range(1,len(arr)):
        maxi+=arr[i]
    print(mini,maxi)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
