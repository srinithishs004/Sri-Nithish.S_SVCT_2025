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
import os
from itertools import combinations

def maxMin(k, arr):
    arr.sort()
    min_unfairness = float('inf')

    for combo in combinations(arr, k):
        current_unfairness = max(combo) - min(combo)
        min_unfairness = min(min_unfairness, current_unfairness)

    return min_unfairness

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

