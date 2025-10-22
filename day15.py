# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, find the
# intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
# return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def get_intersection_node(headA, headB):
    lenA, lenB = get_length(headA), get_length(headB)

    # Advance longer list
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Move both together until intersection
    while headA and headB:
        if headA == headB:  # intersection found
            return headA
        headA = headA.next
        headB = headB.next

    return None

shared = ListNode(8, ListNode(10))

headA = ListNode(3, ListNode(7, shared))

headB = ListNode(99, ListNode(1, shared))

result = get_intersection_node(headA, headB)
print(result.val if result else None)