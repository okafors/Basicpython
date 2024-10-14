def REMOVE(tree, target):
                                                                                            # If the tree is empty, return False (target not found)
    if tree.root is None:
        return False
    
                                                                                             # If the target is the root of the tree
    elif tree.root.data == target:
                                                                                            # If the root has no children, delete it
        if tree.root.left is None and tree.root.right is None:
            tree.root = None
                                                                                            # If the root has only a left child, promote it to the root
        elif tree.root.left and tree.root.right is None:
            tree.root = tree.root.left
                                                                                            # If the root has only a right child, promote it to the root
        elif tree.root.left is None and tree.root.right:
            tree.root = tree.root.right
                                                                                            # If the root has both left and right children, call helper function
        elif tree.root.left and tree.root.right:
            _remove_n_with_left_and_right_children(tree.root)
            
                                                                                            # If the target is not the root of the tree
    else:
        parent = None
        n = tree.root
        
                                                                                            # Traverse the tree to find the n with the target value
        while n and n.data != target:
            parent = n
            if target < n.data:
                n = n.left
            elif target > n.data:
                n = n.right
        
                                                                                            # If the n is not found, return False (target not found)
        if n is None or n.data != target:
            return False
        
                                                                                            # CASE 1: Target has no children
        if n.left is None and n.right is None:
            if target < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
        
                                                                                            # CASE 2: Target has left child only
        elif n.left and n.right is None:
            if target < parent.data:
                parent.left = n.left
            else:
                parent.right = n.left
            return True
        
                                                                                            # CASE 3: Target has right child only
        elif n.right and n.left is None:
            if target < parent.data:
                parent.left = n.right
            else:
                parent.right = n.right
            return True
        
                                                                                            # CASE 4: Target has right child only (not implemented)
                                                                                            # This case is not implemented in this code. It can be added by the user.
        
                                                                                            # CASE 5: Target has left and right children
        else:
            _remove_n_with_left_and_right_children(n)
    
    
def _remove_n_with_left_and_right_children(n):
    """
    Helper function to remove a n with both left and right children.
    """
    delnParent = n
    deln = n.right
    
                                                                                            # Find the minimum n in the right subtree
    while deln.left:
        delnParent = deln
        deln = deln.left
        
                                                                                            # Replace the target n's data with the minimum n's data
    n.data = deln.data
    
                                                                                            # If the minimum n has a right child, promote it to the minimum n's position
    if deln.right:
        if delnParent.data > deln.data:
            delnParent.left = deln.right
        else:
            delnParent.right = deln.right
    
                                                                                            # If the minimum n has no children, delete it
    else:
        if deln.data < delnParent.data:
            delnParent.left = None
        else:
            delnParent.right = None
        def REMOVE(tree, target):
    # If the tree is empty, return False (target not found)
    if tree.root is None:
        return False
    
    # If the target is the root of the tree
    elif tree.root.data == target:
        # If the root has no children, delete it
        if tree.root.left is None and tree.root.right is None:
            tree.root = None
        # If the root has only a left child, promote it to the root
        elif tree.root.left and tree.root.right is None:
            tree.root = tree.root.left
        # If the root has only a right child, promote it to the root
        elif tree.root.left is None and tree.root.right:
            tree.root = tree.root.right
        # If the root has both left and right children, call helper function
        elif tree.root.left and tree.root.right:
            _remove_n_with_left_and_right_children(tree.root)
            
    # If the target is not the root of the tree
    else:
        parent = None
        n = tree.root
        
        # Traverse the tree to find the n with the target value
        while n and n.data != target:
            parent = n
            if target < n.data:
                n = n.left
            elif target > n.data:
                n = n.right
        
        # If the n is not found, return False (target not found)
        if n is None or n.data != target:
            return False
        
        # CASE 1: Target has no children
        if n.left is None and n.right is None:
            if target < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
        
        # CASE 2: Target has left child only
        elif n.left and n.right is None:
            if target < parent.data:
                parent.left = n.left
            else:
                parent.right = n.left
            return True
        
        # CASE 3: Target has right child only
        elif n.right and n.left is None:
            if target < parent.data:
                parent.left = n.right
            else:
                parent.right = n.right
            return True
        
        # CASE 4: Target has right child only (not implemented)
        # This case is not implemented in this code. It can be added by the user.
        
        # CASE 5: Target has left and right children
        else:
            _remove_n_with_left_and_right_children(n)
    
    
def _remove_n_with_left_and_right_children(n):
    """
    Helper function to remove a n with both left and right children.
    """
    delnParent = n
    deln = n.right
    
    # Find the minimum n in the right subtree
    while deln.left:
        delnParent = deln
        deln = deln.left
        
    # Replace the target n's data with the minimum n's data
    n.data = deln.data
    
    # If the minimum n has a right child, promote it to the minimum n's position
    if deln.right:
        if delnParent.data > deln.data:
            delnParent.left = deln.right
        else:
            delnParent.right = deln.right
    
    # If the minimum n has no children, delete it
    else:
        if deln.data < delnParent.data:
            delnParent.left = None
        else:
            delnParent.right = None

