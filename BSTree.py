from binarytree import bst

# Create a random BST
# of any height
root = bst()
print('BST of any height : \n',
      root)

# Create a random BST of
# given height
root2 = bst(height=2)
print('BST of given height : \n',
      root2)

# Create a random perfect
# BST of given height
root3 = bst(height=2,
            is_perfect=True)
print('Perfect BST of given height : \n',
      root3)