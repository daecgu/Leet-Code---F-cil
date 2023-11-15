from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(lst):
    # Crear un nodo inicial que actuará como la cabeza de la lista enlazada
    dummy = ListNode()
    current = dummy

    # Iterar a través de la lista de Python y crear nodos para cada valor
    for value in lst:
        current.next = ListNode(value)
        current = current.next

    # Devolver la cabeza de la lista enlazada
    return dummy.next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next=list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next


lista1 = create_linked_list([1,2,4])
lista2 = create_linked_list([1,3,4])
print(mergeTwoLists(lista1,lista2))