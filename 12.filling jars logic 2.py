# Animesh has  empty candy jars, numbered from  to , with infinite capacity. He performs  operations. Each operation is described by  integers, , , and . Here,  and  are indices of the jars, and  is the number of candies to be added inside each jar whose index lies between  and  (both inclusive). Can you tell the average number of candies after  operations?

# Example



# The array has  elements that all start at . In the first operation, add  to the first  elements. Now the array is . In the second operation, add  to the last  elements (3 - 5). Now the array is  and the average is 10. Sincd 10 is already an integer value, it does not need to be rounded.

# Function Description

# Complete the solve function in the editor below.

# solve has the following parameters:

# int n: the number of candy jars
# int operations[m][3]: a 2-dimensional array of operations
# Returns

# int: the floor of the average number of canidies in all jars
# Input Format

# The first line contains two integers,  and , separated by a single space.
#  lines follow. Each of them contains three integers, , , and , separated by spaces.

# Constraints





# Sample Input

# STDIN       Function
# -----       --------
# 5 3         n = 5, operations[] size = 3
# 1 2 100     operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
# 2 5 100
# 3 4 100
# Sample Output

# 160
#!/bin/python3

def solve(n, operations):
    """
    Calculates the average number of candies in the jars after the operations.

    Args:
        n: The number of candy jars.
        operations: A list of operations, where each operation is a tuple (a, b, k).

    Returns:
        The floor of the average number of candies in all jars.
    """

    total_candies = 0  # Initialize the total number of candies

    for a, b, k in operations:  # Unpack values directly in the loop
        jars_affected = b - a + 1  # Calculate the number of jars involved
        candies_added = k * jars_affected  # Calculate total candies added
        total_candies += candies_added  # Add to the overall total

    average = total_candies // n  # Calculate the floor of the average using integer division
    return average  # Return the integer result

# Example usage:
n = 5
operations = [(1, 2, 100), (2, 5, 100), (3, 4, 100)]
result = solve(n, operations)
print(result)  # Output: 160
