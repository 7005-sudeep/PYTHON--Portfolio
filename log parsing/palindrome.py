#Slicing [::-1] is the "Pythonic" way to reverse data

import re

def is_valid_palindrome(packet_data):
    try:
        # 1. CLEANING: Use re.sub to keep only alphanumeric characters
        # [^a-zA-Z0-9] means "anything NOT a letter or number"
        clean_data = re.sub(r'[^a-zA-Z0-9]', '', str(packet_data)).lower()
        
        # 2. SYMMETRY CHECK: The Python "Slicing" trick
        # [::-1] creates a reversed copy of the string
        is_symmetric = (clean_data == clean_data[::-1])
        
        if is_symmetric:
            print(f"✅ Success: Packet '{packet_data}' is symmetrical.")
        else:
            print(f"❌ Warning: Packet '{packet_data}' is corrupted/asymmetric.")
            
        return is_symmetric

    except Exception as e:
        print(f"❌ Error processing packet: {e}")

# Test cases for WINLAB
is_valid_palindrome("A1-B2-B2-A1") # Should be True
is_valid_palindrome("0xAA 0xBB 0xCC") # Should be False
