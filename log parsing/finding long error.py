#here in this ciode while not s.startswith(prefix): This is a shrinking loop. You keep shaving off the edge until it finally fits.

# secondlhy reversing [:-1]


def find_common_hierarchy(path_list):
    try:
        if not path_list:
            return ""

        # 1. Start by assuming the first path is the prefix
        prefix = path_list[0]

        # 2. Compare this prefix with every other path in the list
        for s in path_list[1:]:
            # While the current string doesn't start with our prefix...
            while not s.startswith(prefix):
                # ...shorten the prefix by one character from the end
                prefix = prefix[:-1]
                
                # If we shorten it to nothing, there is no common prefix
                if not prefix:
                    return "No common hierarchy found."
        
        return prefix

    except Exception as e:
        return f"Error: {e}"

# Test it
hierarchies = ["top.cpu.alu", "top.cpu.fpu", "top.cpu.mmu"]
print(f"Result: {find_common_hierarchy(hierarchies)}")
