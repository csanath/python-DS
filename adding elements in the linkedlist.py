#ADD/INSERT ELEMENTS IN SINGLY LL
class Node:

    def __init__(self,data):
        self.data=data
        self.ref=None
class Linklist:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head==None:
            print("LL is empty")
        else:
            n=self.head
        while n is not None:
            print(n.data)
            n=n.ref

    def add_begin(self,data):                   #adding elemnt in the beginning of ll

        new_node=Node(data)                     #creating new node in beginning
        new_node.ref=self.head               #old head nte value new node n koduthu appo ath 2nd node ilootilla reference aayi
        self.head=new_node                  #refrence of new node is stored in the head

ll=Linklist()

ll.add_begin(10)
ll.add_begin(20)

ll.print_ll()
        
