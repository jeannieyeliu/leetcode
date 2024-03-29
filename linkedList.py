class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def create_linklist(self, arr: list):
        self.val = arr.pop(0)
        currNode = self;
        for val in arr:
            nextNodde = ListNode(val)
            currNode.next = nextNodde;
            currNode = nextNodde

    def printLL(self):
        head = self

        while (head):
            print(head.val, end=", ")
            head = head.next

        print("")

    def append(self, arr):
        curr = self
        for a in arr:
            node = ListNode(a)
            curr.next = node
            curr = node
