# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcp(self, a: int, b: int):
        while a != 0 and b != 0:
            if a < b:
                a, b = b, a
                continue
            else:
                a %= b
        return max(a, b)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next is not None:
            next_node = node.next
            newNode = ListNode(self.gcp(node.val, next_node.val))
            node.next = newNode
            newNode.next = next_node
            node = next_node
        return head
                    