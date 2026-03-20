#here in rhis code we just me entire belt 0 bits and result tells us howmany bits required to amke it entire 0 using and opertor


def count_set_bits(n):
    count = 0
    
    # Keep going as long as there is at least one '1' left
    while n > 0:
        # 1. Use your 'AND' logic to check if LSB is 1
        if n & 1:
            count += 1
            
        # 2. Use your 'Shift' logic to move the next bit to the LSB
        n >>= 1
        
    return count

# --- Testbench ---
# Binary: 1011 (Decimal 11)
# Expect: 3 bits
print(f"Parity Count for 11: {count_set_bits(11)}")

# Binary: 10000000 (Decimal 128)
# Expect: 1 bit
print(f"Parity Count for 128: {count_set_bits(128)}")
