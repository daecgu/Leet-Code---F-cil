# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    #Establecemos una copia de head para no tocar head,
    #como vamos a ir iterando sobre los objetos que itera head, vamos a ir modificando toda la lista
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head