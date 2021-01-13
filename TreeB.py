class Tree(object):
    from binarytree import heap


    root = heap()
    print('Max-heap of any height : \n',
          root)


    root2 = heap(height=2)

    print('Max-heap of given height : \n',
          root2)


    root3 = heap(height=2,is_max=False, is_perfect=True)

    print('Perfect min-heap of given height : \n',root3)