# Given three values, return a new linked list containing those values. You have to wrap the values into ListNode() objects.
# JavaScript:
# const new_node = new ListNode(n);
# Python:
# new_node = ListNode(n)
# You do not need to uncomment the ListNode code in the header. That's just there for your reference.
# Note the the tests will show the linked lists as if they are arrays. This is just the visual representation; 
# under the hood, it's a linked list with those values. Return a reference to the head of the new list.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def solution(a, b, c):
    
    a_node = ListNode(a)
    b_node = ListNode(b)
    c_node = ListNode(c)
    
    a_node.next = b_node
    b_node.next = c_node
    
    return a_node


# Above function generalize
def solution(a, b, c):
    nums = [a, b, c]
    
    head = tail = None
    
    for n in nums:
        new_node = ListNode(n)
        
        if head == None:
            head = tail = new_node
        
        else:
            tail.next = new_node
            tail = new_node
    
    return head


# 
