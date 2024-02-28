'''
find the point
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findPoint' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER px
#  2. INTEGER py
#  3. INTEGER qx
#  4. INTEGER qy
#


def findPoint(px, py, qx, qy):
    # Swap px and qx to achieve reflection
    rx = qx
    ry = qy
    return rx, ry

if __name__ == '__main__':
    # Open the output file in write mode
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of sets of points
    n = int(input().strip())

    for _ in range(n):
        # Read the coordinates of points p and q
        first_multiple_input = input().rstrip().split()
        px = int(first_multiple_input[0])
        py = int(first_multiple_input[1])
        qx = int(first_multiple_input[2])
        qy = int(first_multiple_input[3])

        # Use the modified findPoint function
        result = findPoint(px+1, py+1, qx+1, qy+1)

        # Write the result to the output file
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    # Close the output file
    fptr.close()
