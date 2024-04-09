class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.last=None
    def add_last(self,item):
        node=Node(item)
        if self.head==None:
            self.head=node
            self.last=node
        else:
            self.last.next=node
            self.last=node
    def add_first(self,item):
        node=Node(item)
        node.next=self.head
        self.head=node
    def add_after(self,key,item):
        curr=self.head
        p=0
        while curr:
            if curr.data==key:
                p=1
                break
            curr=curr.next
        if p==0:
            print("data not found")
        else:
            node=Node(item)
            node.next=curr.next
            curr.next=node
    def delete(self,item):
        if self.head.data==item:
            self.head=self.head.next
            return
        curr=self.head
        prev=None
        e=0
        while curr:
            if curr.data==item:
                prev.next=curr.next
                e=e+1
                break
            prev = curr
            curr=curr.next
        if e==0:
            print("Not found")


    def __str__(self):
        r=[]
        curr=self.head
        while curr:
            r.append(curr.data)
            curr=curr.next
        return str(r)

ob=linkedlist()

while True:
    print("----Menu-----""\n""1.Add data Last""\n""2.Add data First""\n""3.Add Data after a element""\n""4.delete Data",
          "\n""5.print data""\n""6.exit""\n""choose menu: ")
    m = int(input())
    if m==1:
        print("Data: ")
        n=int(input())
        ob.add_last(n)
    elif m==2:
        print("Data: ")
        n = int(input())
        ob.add_first(n)
    elif m==3:
        print("key,element: ")
        n,m=map(int,input().split())
        ob.add_after(n,m)
    elif m==4:
        print("Data: ")
        n = int(input())
        ob.delete(n)
    elif m==5:
        print(ob)
    else:
        break