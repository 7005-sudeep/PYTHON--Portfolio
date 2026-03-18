def find_single_number(nums):
    unique_id = 0
    
    # XOR every number in the list
    for num in nums:
        unique_id ^= num  # This is shorthand for unique_id = unique_id ^ num
        
    return unique_id

# Practice Case
id_logs = [102, 55, 102, 88, 55]
# 102 cancels 102, 55 cancels 55. Only 88 remains.

print(f"The unique ID is: {find_single_number(id_logs)}")
# Output: 88
