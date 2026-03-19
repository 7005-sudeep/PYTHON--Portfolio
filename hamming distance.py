def hamming_distance(reg_a, reg_b):
    # 1. Use XOR to find which bits are different
    # If reg_a is 101 and reg_b is 100, diff will be 001
    diff = reg_a ^ reg_b
    
    count = 0
    # 2. Loop to count the '1's in the diff
    while diff > 0:
        # Check if LSB is 1 (Using your AND logic)
        count += (diff & 1)
        
        # Shift right to check the next bit (Using your Shift logic)
        diff >>= 1
        
    return count

# --- Testbench ---
master_val = 0b1101  # (Decimal 13)
slave_val  = 0b1001  # (Decimal 9)
# Bits are different at the 2nd position (index 2)
print(f"Hamming Distance: {hamming_distance(master_val, slave_val)}")
# Output: 1
