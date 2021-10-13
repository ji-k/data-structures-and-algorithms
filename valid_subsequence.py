# VALID SUBSEQUENCE
# EASY

"""
PROBLEM
[] Given two arrays of integers, array and subsequence, write a function that determines whether the second array is a subsequence of the first one.
[] A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array, but that are in the same order as they appear in the array.

CQs
[] Are are getting numbers in the array always? Yes
[] Can we get an empty array? Yes

IO
    0  1   2  V(4)  0  V(1)
[] [1, 0, -5, 20], [0, 10] => true
[] False
[] Edge cases
[] [1, 4, 5], [] => true

Pseudocode
Declare two index pointers to 0
While our indexes are less than the length of the arrays
    Check if current array num equals current subsequence num
        If so, increase subIdx and arrIdx
        If not, increase arrIdx
While finishing loop...
    Return true if subIdx equals the length of the subsequence
    Return false if not
"""

# Code


def validSubsequence(array, subsequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(subsequence):
        if (array[arrIdx] == subsequence[seqIdx]):
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(subsequence)
