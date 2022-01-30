#!/bin/python3
# https://www.hackerrank.com/challenges/electronics-shop/problem


def getMoneySpent(keyboards, drives, budget):
    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #
    sorted_keyboards = sorted(keyboards)
    sorted_drives = sorted(drives)
    totals = list()
    keyboard_index = len(keyboards)
    drive_index = -1
    while keyboard_index > 0:
        keyboard_index -= 1
        keyboard_price = sorted_keyboards[keyboard_index]
        while (drive_index + 1) < len(drives) and keyboard_price + sorted_drives[drive_index + 1] <= budget:
            drive_index += 1
            drive_price = sorted_drives[drive_index]
            totals.append(keyboard_price + drive_price)
    if drive_index == -1:
        return -1
    return max(totals)


if __name__ == "__main__":
    bnm = input().split()
    budget = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    print(getMoneySpent(keyboards, drives, budget))
