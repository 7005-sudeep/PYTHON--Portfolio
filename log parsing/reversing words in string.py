def reverse_packet_header(header):
    try:
        # 1. Split into a list of words based on the dot
        words = header.split('.')
        
        # 2. Reverse the list itself
        words.reverse()
        
        # 3. Join back together
        return ".".join(words)
        
    except Exception as e:
        return f"Error: {e}"

# Test
packet = "source.destination.data.type"
print(reverse_packet_header(packet))
# Output: type.data.destination.source
