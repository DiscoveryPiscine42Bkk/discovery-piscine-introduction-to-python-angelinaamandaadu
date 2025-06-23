#!/usr/bin/env python3

# Original array
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# New array with +2 only for values > 5
new_array = [x + 2 for x in original_array if x > 5]

# Print both arrays
print(original_array)
print(new_array)