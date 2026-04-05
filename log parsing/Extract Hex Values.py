import re

# 1. Compile Pattern (Fast)
hex_regex = re.compile(r"0x[0-9a-f]+", re.IGNORECASE)

# 2. Open with safety flags
with open("huge_sim_log.log", "r", encoding='utf-8', errors='ignore') as f:
    for line in f:
        # 3. Find all hex values in the current line
        addresses = hex_regex.findall(line)
        
        if addresses:
            # 4. Do something with the addresses (e.g., print them)
            for addr in addresses:
                print(f"Found Address: {addr}")


#with try-except method
import re

# 1. Compile outside for speed
hex_regex = re.compile(r"0x[0-9a-f]+", re.IGNORECASE)

def process_log(file_path):
    try:
        # THE TRY BLOCK: Everything that COULD fail goes here
        with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
            for line in f:
                addresses = hex_regex.findall(line)
                if addresses:
                    for addr in addresses:
                        print(f"Found Address: {addr}")

    except FileNotFoundError:
        # Runs if the file name is wrong or the simulation didn't run
        print(f"❌ Error: The file '{file_path}' was not found.")
        
    except PermissionError:
        # Runs if the file is locked by another tool (like the RTL simulator)
        print("❌ Error: You do not have permission to read this file.")
        
    except Exception as e:
        # The "Safety Net" for any other weird errors
        print(f"❌ An unexpected error occurred: {e}")

# Call the function
process_log("huge_sim_log.log")
