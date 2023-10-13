class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None

class SinglyLinkedList:

    def __init__(self) -> None:
        self.head_node = None

    def get_head(self):
        return self.head_node
    
    def insert_node(self, node) -> None:
        if self.head_node is None:
            self.head_node = node
        else:
            curr_node = self.head_node
            while curr_node.next_node:
                curr_node = curr_node.next_node
            curr_node.next_node = node
        return
    
    def __str__(self):
        node = self.head_node
        s=None
        while node:
            s = f"{s}->{node.data}" if s else f"{node.data}"
            node = node.next_node
        s = f"{s}->None"
        return s
    
if __name__ == '__main__':
    # create a sample singly linked list
    ll = SinglyLinkedList()
    val = [10,9,4,6]
    for v in val:
        ll.insert_node(Node(v))
    print(ll)