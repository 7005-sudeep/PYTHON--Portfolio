def merge_sorted_arrays(list1, list2):
    # Initialize pointers for both lists
    i = 0  # Pointer for list1
    j = 0  # Pointer for list2
    merged = []

    # Compare elements one by one until one list is exhausted
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1  # Move list1 pointer
        else:
            merged.append(list2[j])
            j += 1  # Move list2 pointer

    # If list1 still has elements left, add them to the end
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # If list2 still has elements left, add them to the end
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

# Example Practice
a = [1, 4, 7]
b = [2, 3, 8, 9]
print(f"Merged Result: {merge_sorted_arrays(a, b)}")
# Output: [1, 2, 3, 4, 7, 8, 9]
