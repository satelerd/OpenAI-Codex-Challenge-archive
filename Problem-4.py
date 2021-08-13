"""
Problem 4
Parse the given Python source code and return the list of full-qualified paths for all imported symbols, sorted in ascending lexicographic order.

CONSTRAINTS
The input will not contain any wildcard imports (from ... import *).

Ignore aliases (renamings): from x import y as z should be represented as x.y.

LIBRARY SUGGESTION
Consider using the ast module.

EXAMPLES
Input

import os
import concurrent.futures
from os import path as renamed_path
from typing import (
    List, Tuple
)
Output

['concurrent.futures', 'os', 'os.path', 'typing.List', 'typing.Tuple']

"""



import ast
from typing import List


def parse_imports(code: str) -> List[str]:
    tree = ast.parse(code)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.append(name.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module
            names = []
            for name in node.names:
                names.append(name.name)
                #name += str(name.name)
            for name in names:
                imports.append(f"{module}.{name}")
    return (sorted(imports))



# Examples
print(parse_imports('import os\nimport concurrent.futures\nfrom os import path\nfrom typing import (\n List, Tuple\n)'))
print(parse_imports('import os\nfrom typing import List'))