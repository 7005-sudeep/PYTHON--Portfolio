def find_single_number(nums):
    # Initialize our "Accumulator" to 0
    # In hardware: res = 0;
    res = 0
    
    for x in nums:
        # Apply XOR: res = res ^ x #xor gate truth table#
        res =res ^ x
        
    return res

# Test Case (A stream of Transaction IDs)
# Notice: 2 appears twice, 3 appears twice. 4 is unique.
bus_ids = [2, 3, 2, 4, 3]
print(f"The unique Transaction ID is: {find_single_number(bus_ids)}")
