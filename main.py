class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def remove_cars(head, target):
    while head is not None and head.value == target:
        head = head.next
    curr = head
    prev = None
    while curr is not None:
        if curr.value == target:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return head


if __name__ == "__main__":
    n4 = Node(3)
    n3 = Node(2, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)

    new_head = remove_cars(n1, 2)
    curr = new_head
    while curr is not None:
        print(curr.value, end=" ")
        curr = curr.next
    print()
