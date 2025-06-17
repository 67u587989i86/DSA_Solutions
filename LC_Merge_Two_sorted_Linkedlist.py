""" You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]                            """



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        head = ListNode()  # dummy node , this will keep appending 
        current = head     # pointer to access one node at one time
        
        t1, t2 = list1, list2
        
        while t1 and t2:
            if t1.val <= t2.val:  #list1.val access the first node of list1
                current.next = t1  # moves the pointer to its next node of list1
                t1 = t1.next                    # access is to the node two now       
            else:
                current.next = t2 
                t2 = t2.next

            current = current.next # this makes an empty node ahead of merged list inshort initializing an empty node to store something which we will add forward
        
        # Append remaining nodes of t1 or t2 which wont remain any node to compare
        # it is obvious that it is bigger hence didnot passed the while-if/else condition hence appending it to the last
        if t1:
            current.next = t1
        if t2:
            current.next = t2
        
        return head.next # as we started head with null the first node will give 0 , hence we start list from head.next
        