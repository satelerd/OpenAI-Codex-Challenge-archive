"""
Problem 1
Given a the contents of a CSV file as csv_contents, return the difference in days between the date of the earliest and the oldest entry.

The CSV file starts with a header row, which contains at least one column called Date.

You are optionally provided with the pandas library if you need it.

EXAMPLES
Input	"Date,Price,Volume\n2014-01-27,550.50,1387\n2014-06-23,910.83,4361\n2014-05-20,604.51,5870"
Output	147
Explanation	There are 147 days between 2014-01-27 and 2014-06-23.
"""



import itertools
from typing import List


def count_arrangements(sizes: List[int]) -> int:
    if len(sizes) < 2:
        return 0
        
    #Order the list from higher to lowest
    sizes.sort(reverse=True)
    #Get all the possible combinations
    combinations = list(itertools.permutations(sizes, len(sizes)))
    combinations = [combination for combination in combinations if combination[0] > combination[1]]
    print(combinations)
    #Count the number of combinations
    return len(combinations)

# Examples
print(count_arrangements([1, 3, 1]))
print(count_arrangements([1, 2]))