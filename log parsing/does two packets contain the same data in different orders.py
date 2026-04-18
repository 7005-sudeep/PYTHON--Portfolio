#.replace(" ", ""): This searches for any empty spaces and removes them. It turns "TX DATA" into "TXDATA"
#.lower(): This turns everything into lowercase. It ensures "TX" and "tx" are treated as the exact same data.
#if Counter(p1_clean) == Counter(p2_clean):
    #Size Check: If p1 has 10 characters and p2 has 9, they are immediately NOT equal.
    #Content Check: If both have 10 characters, but p1 has three As and p2 only has two As, they are NOT equal

from collections import Counter 

def check_packet_integrity(packet1, packet2):
    try:
        # 1. Standardize: Remove spaces and make lowercase
        # This ensures 'Data' and 'data ' are treated as the same
        p1_clean = packet1.replace(" ", "").lower()
        p2_clean = packet2.replace(" ", "").lower()

        # 2. Compare Frequencies
        # Counter creates a 'scoreboard' for each packet
        if Counter(p1_clean) == Counter(p2_clean):
            return True
        else:
            return False

    except Exception as e:
        return f"Processing Error: {e}"

# Test Cases
pkt_sent = "TX_DATA_01"
pkt_recv = "01_DATA_TX"

if check_packet_integrity(pkt_sent, pkt_recv):
    print("✅ Success: Data is intact (Anagram)")
else:
    print("❌ Fail: Data was corrupted or changed")
