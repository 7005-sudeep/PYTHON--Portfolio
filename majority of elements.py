def get_majority(nums):
    candidate = nums[0]  # Assigning the 1st value to our variable
    count = 1            # Initial count for the 1st value
    
    # We start checking from the 2nd element (index 1) onwards
    for i in range(1, len(nums)):
        if count == 0:
            candidate = nums[i] # New candidate if previous one was "voted out"
            count = 1
        elif nums[i] == candidate:
            count += 1          # Same value? Increment!
        else:
            count -= 1          # Different value? Decrement!
            
    return candidate

# Test Case
data_stream = [2, 2, 1, 1, 1, 2, 2]
print(f"The winning Transaction ID is: {get_majority(data_stream)}")
