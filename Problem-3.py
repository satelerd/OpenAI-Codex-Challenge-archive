"""
Problem 3
Given a compressed message compressed and the prefix code tree used to encode it, decode and return the original message.

tree is a nested dictionary with characters at the leaves. For each character in compressed, traverse down one step of the tree. Once you reach a leaf of the tree, the character at that leaf is appended to the decoded message.

If the compressed message could not be decoded in full because the last step did not end at a leaf, return what was decoded so far.

CONSTRAINTS
The keys of tree and its subdictionaries are always '0' or '1', and the leaf values are also always single characters.

EXAMPLES
Input	compressed = "110100100" tree = {"0": "a", "1": {"0": "n", "1": "b"}}
Output	"banana"
Input	compressed = "0111010100" tree = {"0": {"0": "x", "1": "z"}, "1": "y"}
Output	"zyyzzx"
Input	compressed = "000" tree = {"0": {"0": "x", "1": "z"}, "1": "y"}
Output	"x"
"""



from typing import Dict, Union

Tree = Dict[str, Union[str, "Tree"]]


def decompress(compressed: str, tree: Tree) -> str:
    print(compressed)
    print(tree)

    word = ""
    num_ant = -1
    num_ant2 = -1
    num_ant3 = -1
    for num in compressed:
        #print("num: ", num)
        num = str(num)

        if num_ant != -1:
            #print("primer if: ", type(tree[num_ant][num]))
            if num_ant2 != -1:
                if num_ant3 != -1:
                    print(num_ant3)
                    word += tree[num_ant][num_ant2][num_ant3][num]
                    num_ant = -1
                    num_ant2 = -1
                    num_ant3 = -1
                    continue

                print(type(tree[num_ant][num_ant2][num]) == str)
                if type(tree[num_ant][num_ant2][num]) == str:
                    word += tree[num_ant][num_ant2][num]
                    num_ant = -1
                    num_ant2 = -1
                    num_ant3 = -1
                    continue
                else:
                    print("Q sucede")
                    num_ant3 = num
                    continue


            if type(tree[num_ant][num]) == str:
                word += tree[num_ant][num]
                num_ant = -1
                num_ant2 = -1
                num_ant3 = -1
                continue
            else:
                num_ant2 = num
                continue


        if type(tree[num]) == str:
            #print("segundo if: ", tree[num])
            word += tree[num]
            num_ant = -1
            num_ant2 = -1
            num_ant3 = -1
            continue
        else:
            #print("else: ", num)
            num_ant = num
            continue
        
        #print()
        
    return(word)
# Examples
#print(decompress('110100100', {'0': 'a', '1': {'0': 'n', '1': 'b'}}))
# eZkZkkkPZZePPkZkkkkkZkeekZZkkZkkZkkkkkZkkk
#
#print(decompress('11001111000100101110', {'1': {'0': 'w', '1': {'0': 'S', '1': {'1': '2', '0': 'z'}}}, '0': 'T'}))
#ST2TTTwTwz