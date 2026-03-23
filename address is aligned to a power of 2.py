def is_aligned_power_of_two(address):
    # 1. Address must be greater than 0
    # 2. ANDing with predecessor must result in 0
    if address <= 0:
        return False
    
    return (address & (address - 1)) == 0

# --- Testbench ---
print(f"Is 1024 aligned? {is_aligned_power_of_two(1024)}") # True
print(f"Is 1025 aligned? {is_aligned_power_of_two(1025)}") # False 

# jsut need to check address is not eual to zero and address and address-1 and opertion if it is giving zero then it is power of 2 else not 
