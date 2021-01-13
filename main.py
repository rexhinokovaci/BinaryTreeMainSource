class Tree(object):
    from binarytree import Node
    root = Node(int(input("Enter Root: ")))
    root.left = Node(int(input("Enter Left Subtree: ")))
    root.right = Node(int(input("Enter Right Subtree: ")))


    print('Binary tree :', root)


    print('List of nodes :', list(root))

    print('Inorder of nodes :', root.inorder)


    print('Size of tree :', root.size)
    print('Height of tree :', root.height)

    print('Properties of tree : \n', root.properties)



