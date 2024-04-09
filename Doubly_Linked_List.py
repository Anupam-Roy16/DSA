class Node:
    def __init__(self,item):
        self.data=item
        self.next=None
        self.prev=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.last=None
    def add_last(self,item):
        node=Node(item)
        if self.head==None:
            self.head=node
            self.last=self.head
        else:
            self.last.next=node
            node.prev=self.last
            self.last=node
    def add_first(self,item):
        node=Node(item)
        if self.head == None:
            self.head = node
            self.last = self.head
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
    def add_after(self,key,item):
        curr=self.head
        p=0
        while curr:
            if curr.data==key:
                p=1
                node = Node(item)
                node.next = curr.next
                curr.next.prev = node
                node.prev = curr
                curr.next = node
            curr=curr.next
        if p==0:
            print("data not found")

    def delete(self,item):
        if self.head.data==item:
            self.head=self.head.next
            self.head.prev=None
            return

        curr=self.head
        #prev=None
        e=0
        while curr:
            if curr.data==item:
                curr.prev.next=curr.next
                if curr.next!=None:
                    curr.next.prev=curr.prev
                e=e+1
            curr=curr.next
        if e==0:
            print("Not found")
    def traverse_forward(self):
        curr=self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
        print("\n")
        return
    def traverse_backward(self):
        curr=self.last
        while curr:
            print(curr.data,end=" ")
            curr=curr.prev
        print("\n")
        return
    def __str__(self):
        r=[]
        curr=self.head
        while curr:
            r.append(curr.data)
            curr=curr.next
        return str(r)

ob=linkedlist()

while True:
    print("----Menu-----""\n""1.Add data Last  ""2.Add data First""\n""3.Add Data after a element  ""4.delete Data",
          "\n""5.print data    6.print forward""\n""7.print backward    8.exit""\n""choose menu: ")
    m = int(input())
    if m==1:
        print("Data input (-1 exit): ")
        while True:
            n=int(input())
            if n==-1:
                break
            ob.add_last(n)
    elif m==2:
        print("Data input (-1 exit): ")
        while True:
            n = int(input())
            if n == -1:
                break
            ob.add_first(n)
    elif m==3:
        print("key,element: ")
        n,m=map(int,input().split())
        ob.add_after(n,m)
    elif m==4:
        print("Data input (-1 exit): ")
        while True:
            n = int(input())
            if n == -1:
                break
            ob.delete(n)
    elif m==5:
        print(ob)
    elif m==6:
        ob.traverse_forward()
    elif m==7:
        ob.traverse_backward()
    else:
        break






