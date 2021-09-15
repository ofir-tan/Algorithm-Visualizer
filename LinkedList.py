class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, nodes=None, head=None):
        self.head = head
        self.d = {0: '⊚', 1: '①', 2: '②', 3: '③', 4: '④', 5: '⑤',
                  6: '⑥', 7: '⑦', 8: '⑧', 9: '⑨', 10: '⑩'}
        if nodes is not None:
            node = ListNode(val=nodes.pop(0))
            self.head = node
            for val in nodes:
                node.next = ListNode(val=val)
                node = node.next

    def __len__(self):
        node = self.head
        length = 0
        while node:
            node = node.next
            length += 1
        return length

    def __getitem__(self, k):
        return self.get_Kth(k) if k >= 0 else self.get_kth_from_end(abs(k))

    def __str__(self):
        node = self.head
        s = ''
        while node:
            s += f"{self.d[node.val]} ➪ "
            node = node.next
        return s + 'Ø'

    def reverse(self, k=-1):
        prev = None
        head = self.head
        while head and k:
            next, head.next = head.next, prev
            # update:
            prev, head = head, next
            k -= 1
        self.head = prev

    def get_Kth(self, k):
        node = self.head
        for _ in range(k):
            node = node.next
        return node

    def get_kth_from_end(self, k):
        node = self.get_Kth(k)
        head = self.head
        while node and node.next:
            head, node = head.next, node.next
        return head, node
