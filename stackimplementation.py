stack=[]
def push():
    element=input("enter the element to the stack")
    stack.append(element)
    print(stack)

def popelement():
    if len(stack)==0:
        print("stack is empty")

    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        popelement()
    elif choice==3:
        break
    else:
        print("enter the correct operation!")
        
    
        
    
