def isolate_rightmost_bit(n):
    if n == 0:
        return 0
    
    # Logic: n & (~n + 1) which is n & -n
    return n & -n

# --- Testbench ---
# Input: 12 (Binary: 1100)
# Rightmost bit is 4 (Binary: 0100)
val = 12
result = isolate_rightmost_bit(val)

print(f"Original: {bin(val)} ({val})")
print(f"Isolated: {bin(result)} ({result})")
