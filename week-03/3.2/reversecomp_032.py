#!/usr/bin/env python3

import sys
lines = []
lineslower = []

# Binary search (adapted from CA116)
def binsearch(query, sorted_list):

    '''Return True if query in sorted_list else False'''

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        # print(f'{low} {mid} {high}')

        if sorted_list[mid] < query:
            # Search RHS
            low = mid + 1

        elif sorted_list[mid] > query:
            # Search LHS
            high = mid - 1

        else:
            # Found it
            return True

    # Not found
    return False

for line in sys.stdin:
  lines.append(line.strip())
  lineslower.append(line.lower().strip())

print([word for word in lines if binsearch(word.lower()[::-1], lineslower) and len(word) >= 5])
