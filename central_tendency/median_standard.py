"""
Median of an unsorted array:
To implement a median finder using standard sort (O(n log n)), approach.
"""

from ._registry import register

@register
def median_standard(arr):
    arr = sorted(arr)
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2] + arr[n // 2 - 1]) / 2
    else:
        return arr[n // 2]

