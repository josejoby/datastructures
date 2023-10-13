from singly_linked_list import Node, SinglyLinkedList

# representation using adjacency list approach
class Graph: 
    def __init__(self, vertex_count) -> None:
        self.vertex_count = vertex_count
        self.arr = []
        for _ in range(self.vertex_count):
            self.arr.append(SinglyLinkedList())
    
    def add_edge(self, srcv, destv):
        if 0 <= srcv < len(self.arr) and 0 <= srcv < len(self.arr):
            self.arr[srcv].insert_node(Node(destv))

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertex_count):
            print("|", i, end=" | => ")
            temp = self.arr[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_node
            print("None")

if __name__ == "__main__":
    
    # create a sample graph
    g = Graph(4)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.print_graph()

    # print(g.arr[1].get_head().data)