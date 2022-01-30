#!/bin/python3
# https://www.hackerrank.com/challenges/richie-rich/problem


def highestValuePalindrome(s, n, k):
    # The function is expected to return a STRING.
    # The function accepts following parameters:
    #  1. STRING s
    #  2. INTEGER n
    #  3. INTEGER k
    left_changes = k
    new_string = list(s)

    # Step 1. Make it a palindrome
    changed_indexes = set()
    for i in range(n // 2):
        if left_changes < 1:
            break
        left = new_string[i]
        right = new_string[-i - 1]
        if left < right:
            new_string[i] = right
            changed_indexes.add(i)
            left_changes -= 1
        if right < left:
            new_string[-i - 1] = left
            changed_indexes.add(n - i - 1)
            left_changes -= 1
    if new_string != list(reversed(new_string)):
        # If it's not a palindrome by this point, it will not become one on the optimizations
        return "-1"

    # Step 2. Optimize the palindrome (make it bigger as a number by using more 9s on the left)
    for i in range(n // 2 + 1):
        if left_changes < 1:
            break
        if new_string[i] == "9":
            continue

        is_index_the_exact_middle = i == (n - i - 1)
        is_pair_already_modified = i in changed_indexes or (n - i - 1) in changed_indexes
        if left_changes > 1 or (is_pair_already_modified or is_index_the_exact_middle):
            new_string[i] = new_string[-i - 1] = "9"
            changed_indexes.add(i)
            changed_indexes.add(n - i - 1)
            left_changes = k - len(changed_indexes)

    return "".join(new_string)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = input()

    print(highestValuePalindrome(s, n, k))
