queue=[]
def enqueue():
    element=input("enter the elements")
    queue.append(element)
    print(element,"added to the queue")

def dequeue():
    if len(queue)==0:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print(e,"removed")

def display():
    print(queue)

while True:
    print("select the operation 1.add 2.remove 3.show 4.quit")
    choice=int(input("enter your choice"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter the correct choice!")

        
