# this is for c language implementation        python list  append and pop can crete this
# the draw back of queue(cannot reuse memory) solved by circular queue

class queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None] * self.size
        self.rear = 0
        self.front = 0
    def enque(self,val):
        if self.rear == self.size:
            print("overflow")
            return
        self.queue[self.rear] = val
        self.rear += 1

    def deque(self):
        if self.front == self.rear:
            print("underflow")
            return
        print(self.queue[self.front])
        self.front += 1

num = int(input("queue size: "))
ob = queue(num)
while 1:
    print("1 for enque  2 for dequeu")
    num = int(input("choice: "))
    if num == 1:
        num  = int(input("num: "))
        ob.enque(num)
    elif num == 2:
        ob.deque()
    else:
        print("invalid")