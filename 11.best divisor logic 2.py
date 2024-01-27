# Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

# Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

# Input Format

# A single integer denoting .

# Constraints

# Output Format

# Print an integer denoting the best divisor of .

# Sample Input 0

# 12
# Sample Output 0

# 6
#!/bin/python3
def find_best_divisor(n):
    """
    Finds the divisor of n that has the largest sum of digits,
    and returns the smaller divisor if there's a tie.

    Args:
        n: The number whose divisor is to be found.

    Returns:
        The best divisor of n.
    """

    best_divisor = 1  # Initialize with the first divisor
    best_digit_sum = digit_sum(best_divisor)  # Calculate its digit sum

    for divisor in range(2, n + 1):
        if n % divisor == 0:  # Check if it's a divisor
            current_digit_sum = digit_sum(divisor)
            if current_digit_sum > best_digit_sum:
                best_divisor = divisor
                best_digit_sum = current_digit_sum
            elif current_digit_sum == best_digit_sum and divisor < best_divisor:
                best_divisor = divisor  # Choose the smaller divisor in case of a tie

    return best_divisor

def digit_sum(number):
    """Calculates the sum of digits in a number."""

    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number //= 10
    return sum_of_digits

# Example usage:
n = 180
best_divisor = find_best_divisor(n)
print(best_divisor)  # Output: 9
