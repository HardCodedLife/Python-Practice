class Node:
    def __init__(self, n) -> None:
        self.data = n
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def append(self, node: Node):
        current = self.head
        while current != None:
            if current.next == None:
                current.next = node
                break
            current = current.next
        if self.head == None:
            self.head = node 
    def __str__(self):
        show = ''
        current = self.head
        while current != None:
            show += f'{current.data} -> '
            if current.next == None:
                show += "None"
            current = current.next
        return show
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(Node(10))
    ll.append(Node(20))
    ll.append(Node(30))
    #print(ll.head.data)
    print(ll)
