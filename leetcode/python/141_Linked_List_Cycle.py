"""
	141. Linked List Cycle

	Given a linked list, determine if it has a cycle in it.

	Follow up:
	Can you solve it without using extra space?
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
      
        #fast = ListNode(0)
        #slow = ListNode(1)
        #fast.next = head.next
        #slow.next = head.next
        
        fast = head 
        slow = head

        while fast and fast.next:
        	slow = slow.next
        	fast = fast.next.next
        	if fast:
        		if fast == slow:
        			return True 
        	else:
        		return False
        return False

L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L4 = ListNode(4)

L1.next = L2
L2.next = L3
L3.next = L4
#L4.next = L2

sol = Solution()
print sol.hasCycle(L1)