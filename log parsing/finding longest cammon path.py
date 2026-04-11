import re

def get_common_prefix(paths):
    """
    Finds the longest common hierarchical prefix in a list of paths.
    """
    if not paths: return ""
    
    # Split paths into levels
    split_paths = [re.split(r'\.', p) for p in paths]
    
    # Shortest path is the limit
    base = min(split_paths, key=len)
    
    result = []
    for i in range(len(base)):
        # Check if all paths match at this level
        if all(p[i] == base[i] for p in split_paths):
            result.append(base[i])
        else:
            break
            
    return ".".join(result)
