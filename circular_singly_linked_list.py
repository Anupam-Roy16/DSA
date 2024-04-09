class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

class cir_sing_linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_at_head(self,item):
        node=Node(item)
        if self.head==None:
            self.head=node
            self.tail=node
            self.head.next=self.tail
            self.tail.next=self.head
        else:
            node.next=self.head
            self.tail.next=node
            self.head=node
    def insert_at_tail(self,item):
        node=Node(item)
        if self.head==None:
            self.head=node
            self.tail=node
            self.head.next=self.tail
            self.tail.next=self.head
        else:
            self.tail.next=node
            node.next=self.head
            self.tail=node
    def insert_at_pos(self,pos,item):
        node=Node(item)
        i=0
        if pos==0:
            cir_sing_linkedlist.insert_at_head(self,item)
            return
        tmp=self.head
        while True:
            if i==pos-1:
                break
            tmp=tmp.next
            i=i+1
        node.next=tmp.next
        tmp.next=node


    def delete_head(self):
        if self.head==None:
            print("no value to delete")
            return
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail.next=self.head.next
            self.head=self.head.next
    def delete_tail(self):
        if self.head==None:
            print("no value to delete")
            return
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            tmp=self.head
            while True:
                if tmp.next==self.tail:
                    break
                tmp=tmp.next
            tmp.next=self.head
            self.tail=tmp
    def delete_specific_data(self,pos):
        tmp=self.head
        i=0
        if pos==0:
            cir_sing_linkedlist.delete_head(self)
            return
        while True:
            if i==pos-1:
                break
            tmp=tmp.next
            i=i+1
        tmp.next=tmp.next.next



    def print(self):
        tmp=self.head
        i=0
        if tmp==None:
            print("No value")
            return
        while True:
            print(tmp.data,end=" ")
            tmp=tmp.next
            if tmp==self.head:
                break
        print("\n")

ob=cir_sing_linkedlist()
ob.print()
ob.insert_at_head(12)
ob.print()
ob.insert_at_head(13)
ob.insert_at_head(14)
ob.print()
ob.insert_at_tail(21)
ob.print()
ob.insert_at_tail(0)
ob.insert_at_tail(90)
ob.print()
ob.delete_specific_data(0)
ob.print()
ob.delete_specific_data(0)
ob.print()
ob.insert_at_pos(1,13)
ob.print()
ob.insert_at_pos(0,1)
ob.print()
ob.insert_at_pos(6,91)
ob.print()