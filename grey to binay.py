def gray_to_binary(n):
    mask = n
    while mask > 0:
        mask >>= 1
        n ^= mask
    return n

# Test: Gray '0b010' (which is 3)
# 1. n = 010, mask = 001 -> n = 010 ^ 001 = 011 (Binary 3!)
