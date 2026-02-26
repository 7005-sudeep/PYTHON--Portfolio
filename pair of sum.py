def check_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n): # Start 'j' from the next element
            if nums[i] + nums[j] == target:
                return True
    return False// this is useful when we have limited number of elements //



  
