"""
Problem 2
source and target are two strings each containing file contents. Return the number of lines you would need to insert and the number of lines you would need to delete to get to target from source.

Return your answer as a tuple (inserted, deleted).

LIBRARY SUGGESTION
Consider using the difflib module.

EXAMPLES
Input	source = "Apple\nOrange\nPear" target = "Apple\nPear\nBanana\nMango"
Output	(2, 1)
"""



import difflib
from typing import Tuple


def diff_files(source: str, target: str) -> Tuple[int, int]:
    source_lines = source.splitlines()
    target_lines = target.splitlines()
    print(source_lines, target_lines)

    diff = difflib.ndiff(source_lines, target_lines)
    lines_to_add = 0
    lines_to_delete = 0
    for line in diff:
        if line.startswith('+'):
            lines_to_add += 1
        elif line.startswith('-'):
            lines_to_delete += 1
    return (lines_to_add, lines_to_delete)


# Examples
#print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana\nMango'))
#print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana'))