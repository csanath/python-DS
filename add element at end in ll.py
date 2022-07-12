class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linlist:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
        while n is not None:
            print(n.data,"---->",end=" ")
            n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref=new_node
            n.ref=new_node

ll=Linlist()
ll.add_begin(10)
ll.add_end(100)
ll.add_begin(20)
ll.print_ll()
