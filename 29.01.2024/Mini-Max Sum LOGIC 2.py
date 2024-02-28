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
def miniMaxSum(arr):
    arr.sort()
    mini = sum(arr[:-1])
    maxi = sum(arr[1:])
    print(mini, maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

