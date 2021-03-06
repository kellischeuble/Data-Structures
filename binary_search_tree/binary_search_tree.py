from queue.queue import LinkedListQueue
from stack.stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two parts:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to parent node

        # if passed in value is less than self.value:
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                # repeat the process on left subtree
                self.left.insert(value)
            
        # if pass in value is greater than or equal self.value:
        if value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                # repeat process on right subtree
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if target == self.value:        
            return True

        if target < self.value:
            if not self.left:
                return False
            else:
                # recurse that sh*t
                # gotta return to give the second one
                # a present. otherwise the bool values
                # don't go anywhere. You need to return the
                # returned
                return self.left.contains(target)
        else:
            # if there is not a child to the roit
            if not self.right:
                return False
            else:
                # cirlce cirlce circle     
                return self.right.contains(target)
            

    # Return the maximum value found in the tree
    def get_max(self):
        # look at the node
        # if there isn't a node.right:

        # Recursive approach
        if not self.right:
            return self.value
        return self.right.get_max()

        # iterative approach
        # rightmost leaf is the max value
        # start at top, keep going right until you hit None
        
        # max_value = self.value
        # current = self

        # While current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right

        # return max_value 
                    
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        # call function on value
        fn(self.value)

        if self.left:
            # recurse on all lefts
            self.left.for_each(fn)
        if self.right:
            # recurse on all rights
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):

        # if the current node is None
        # know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return 

        # check if we can move left
        if self.left is not None:
            self.left.in_order_print()

        # visit the node by printing its value
        print(self.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        # use queue to form a "line"   
        queue = LinkedListQueue()

        # start by placicng the root in the queue
        queue.enqueue(node)
        
        # while loop to iterate
        # while length of queue is greater than 0
        while queue.size > 0:
            # dequeue item from front of queue
            current_item = queue.dequeue()
            # print that item
            print(current_item.value)

            # place current item's left node in queue if not None
            if current_item.left is not None:
                queue.enqueue(current_item.left)
            # place current item's right node in queue if not None
            if current_item.right is not None:
                queue.enqueue(current_item.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        stack = Stack()
        stack.push(node)

        while stack.__len__() > 0:
            top_item = stack.pop()
            print(top_item.value)

            if top_item.right is not None:
                stack.push(top_item.right)

            if top_item.left is not None:
                stack.push(top_item.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # visit the node by printing its value
        print(self.value)

        # check if we can "move left"
        if self.left is not None:
            self.left.pre_order_dft(self)

        # check if we can "move right"
        if self.right is not None:
            self.right.pre_order_dft(self)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # check if we can "move left"
        if self.left is not None:
            self.left.post_order_dft(self)

        # check if we can "move right"
        if self.right is not None:
            self.right.post_order_dft(self)

        # visit the node by printing its value
        print(self.value)
