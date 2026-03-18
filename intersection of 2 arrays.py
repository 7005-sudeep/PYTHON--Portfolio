def find_intersection(list1, list2):
    i = 0
    j = 0
    intersection = []
    
    # Loop until we reach the end of either list
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            # Match! Add to result if it's not a duplicate
            if not intersection or list1[i] != intersection[-1]:
                intersection.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            # list1 is lagging behind, move it forward
            i += 1
        else:
            # list2 is lagging behind, move it forward
            j += 1
            
    return intersection

# Practice Case
map_a = [1, 2, 4, 5, 9]
map_b = [2, 3, 5, 7, 9, 10]

print(f"Common Addresses: {find_intersection(map_a, map_b)}")
# Output: [2, 5, 9]
