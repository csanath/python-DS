#LINKED LIST TRAVERSAL 

#1.create node
class node:
    def __init__(self,data):
        self.data=data
    #ref
        self.ref=None

#to link the nodes we need to create another class
class linkedlist:
    def __init__(self):
        self.head=None
    def print_linkedlist(self):
        if self.head is None:
            print("LINKEDLIST IS EMPTY")
        else:
           n=self.head
           #to continue traversal until ref=none;used loop
        while n is not None:
            print(n.data)
            n=n.ref
ll1=linkedlist()
ll1.print_linkedlist()
#this is how linkedlist traversal is done
            
        
