# this is for c language implementation. python list  append and pop can crete this



class stack():
    def __init__(self,size):
        self.size = size
        self.stack = [0]*size
        self.top = 0
    def push(self,val):
        if self.top == self.size:
            print("stack full")
        else:
            self.stack[self.top] = val
            self.top += 1
    def pop(self):
        self.top -= 1
        if self.top < 0:
            print("stack empty")
            return
        return self.stack[self.top]

if __name__ =='__main__':
    size = int(input("stack size: "))
    obj = stack(size)
    while 1:
        print("1 for push 2 for pop:  ")
        n = input()
        if n == '1':
            num = int(input())
            obj.push(num)
        elif n == '2':
            print(obj.pop())
        else:
            print("invalid")