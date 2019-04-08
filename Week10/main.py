#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    array = s.split()
    s = ""
    for i in array:
        s+= i.capitalize() + " "
    return s

if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)