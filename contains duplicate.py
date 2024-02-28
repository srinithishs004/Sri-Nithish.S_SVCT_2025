def contains_duplicate(nums):
   
    unique_elements = set()

    for num in nums:
        if num in unique_elements:
            return True
        else:
            unique_elements.add(num)
    return False

numbers = [1, 2, 3, 4, 5]
result = contains_duplicate(numbers)
print("Contains Duplicate:", result)