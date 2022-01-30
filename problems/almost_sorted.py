#!/bin/python3
# https://www.hackerrank.com/challenges/almost-sorted/problem


def almostSorted(arr):
    #
    # The function accepts INTEGER_ARRAY arr as parameter.
    #
    misplaced = [a for a, (i, j) in enumerate(zip(arr, sorted(arr))) if i != j]
    # It's already sorted?
    if len(misplaced) == 0:
        return "yes"
    # Swapping
    if len(misplaced) == 2:
        return f"yes\nswap {misplaced[0] + 1} {misplaced[1] + 1}"
    # Reversing sub-array
    if len(misplaced) > 2:
        fragment = arr[misplaced[0] : misplaced[-1] + 1]
        if fragment == sorted(fragment, reverse=True):
            return f"yes\nreverse {misplaced[0] + 1} {misplaced[-1] + 1}"
    # Not possible
    return "no"


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    print(almostSorted(arr))
