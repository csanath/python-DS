#LINKED LIST TRAVERSAL 

#creating node
class node::
    def __init__(self,data)
        self.data=data
    
        self.ref=None  #ref

#to link the nodes we need to create another class
class linkedlist:
    def __init__(self):
        self.head=None
    def print_linkedlist(self):
        if self.head is None:
            print("LINKEDLIST IS EMPTY")
        else:
           n=self.head
           
        while n is not None: #to continue traversal until ref=none;used loop
            print(n.data)
            n=n.ref
ll1=linkedlist()
ll1.print_linkedlist()
#this is how linkedlist traversal is done
            
        
