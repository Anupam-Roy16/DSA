class infix_to_prefix:
    def __init__(self,str):
        self.str = str
        self.stack = []
        self.res = []
    def precedence(self,opr):
        if opr == '+' or opr == '-':
            return 1
        else:
            return 2
    def function(self):
        for chr in self.str:
            if chr == '(':
                self.stack.append('(')
            elif (chr >= '0' and chr <= '9'):
                self.res.append(chr)
            elif chr == ')':
                while self.stack:
                    if self.stack[-1] == '(':
                        self.stack.pop()
                        break
                    else:
                        self.res.append(self.stack[-1])
                        self.stack.pop()
            else:
                while self.stack:
                    if self.stack[-1] == '(':
                        break
                    else:
                        if self.precedence(chr) <= self.precedence(self.stack[-1]):
                            self.res.append(self.stack[-1])
                            self.stack.pop()
                        else:
                            break
                self.stack += chr
        while self.stack:
            self.res.append(self.stack.pop())
        return self.res

obj = infix_to_prefix("(2+3)*5/6")
print(obj.function())