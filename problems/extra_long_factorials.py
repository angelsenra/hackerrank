#!/bin/python3
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#
# FIXME: Do in the "hard" way

def extraLongFactorials(n):
    # Write your code here
    if n == 1:
        return 1
    return n * extraLongFactorials(n - 1)

if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))
