# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = []
        current = self
        # print('ListNode current000', current)
        while current:
            result.append(current.val)
            # print('ListNode result', result)
            current = current.next
            # print('ListNode current111', current)
            print('rrrrrrrrrrresult', result, '\n')
        return "->".join(map(str, result))


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Count the number of nodes and find the tail
        count, tail = 1, head
        print('count', count, 'tail', tail, '\n')
        print('tail.nex', tail.next,'\n')
        while tail.next:
            count += 1
            tail = tail.next
            print('count', count, 'tb  ail', tail, '\n')

        # Find the effective rotations needed
        k %= count
        print('K %', k)
        if k == 0:
            print('head000', head, '\n')
            return head
        

        # Find the new tail: (count - k - 1)th node
        new_tail = head
        print('new_tail', new_tail, '\n')
        for _ in range(count - k - 1):
            new_tail = new_tail.next
            print('new_tail000', new_tail, '\n')

        # New head is the next node of the new tail
        new_head = new_tail.next
        print('new_tail111', new_head, '\n')
        new_tail.next = None
        tail.next = head  # Link old tail to the original hea
        print('new_tail111', new_head, '\n')
        return new_head


# Helper function to create a linked list from a Python list
def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    print('head', head, '\n')
    current = head
    # print('current', current, '\n')
    for value in values[1:]:
        print('value', value, '\n')
        print('currentrrrrrrr', current)
        current.next = ListNode(value)
        print('current.next', current.next, '\n')
        current = current.next
    print('head0000000000', head,'\n')
    return head


# Helper function to convert linked list to a Python list (for printing)
def print_linked_list(head: Optional[ListNode]) -> None:
    if not head:
        print("Empty list\n")
        return
    print(str(head))


# Test the function
if __name__ == "__main__":
    # Input linked list and k
    input_list = [1, 2, 3, 4, 5]
    k = 2

    # Create the linked list
    head = create_linked_list(input_list)

    # Create a Solution instance and call rotateRight
    solution = Solution()
    rotated_head = solution.rotateRight(head, k)

    # Print the rotated linked list
    print_linked_list(rotated_head)
