'''
Max Min
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    min_unfairness = float('inf')

    for i in range(len(arr) - k + 1):
        current_unfairness = arr[i + k - 1] - arr[i]
        min_unfairness = min(min_unfairness, current_unfairness)

    return min_unfairness
print(maxMin(3, [10, 100, 300, 200, 1000, 20, 30])) 
print(maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))
print(maxMin(2, [1, 2, 1, 2, 1]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
