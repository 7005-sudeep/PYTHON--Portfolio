# here for this problem i need to first calulte the width for which i have to extract then mask it simply left shift by width then subtract 1
# then simply again right shift this value by lsb then make and oprtion with the mask value we will get extract bits from overall bit value

def extract_bitfield(val, high, low):
    # 1. Calculate the width of the field
    width = high - low + 1
    
    # 2. Create a mask of '1's for that width
    # Example: if width is 4, (1 << 4) is 10000. Subtract 1 to get 01111 (0xF)
    mask = (1 << width) - 1
    
    # 3. Shift the value down and apply the mask
    return (val >> lower bit(lsb)) & mask

# --- Testbench ---
# Input: 0xABCD (Binary: 1010 1011 1100 1101)
# Extract bits [7:4] -> Should be 0xC (1100)
val = 0xABCD
result = extract_bitfield(val, 7, 4)

print(f"Value:  {hex(val)}")
print(f"Result: {hex(result)}") # Expect 0xc
