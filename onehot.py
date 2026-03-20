def is_one_hot(n):
    # Reuse your bit counter!
    if count_set_bits(n) == 1:
        return True
    return False

# Example:
# 0b0001 -> True (One-Hot)
# 0b1010 -> False (Two bits are high)
