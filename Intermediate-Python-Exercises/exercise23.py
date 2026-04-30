class my_stack:
    def __init__(self) -> None:
        self.stack = []
    def push(self, e):
        self.stack.append(e)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
if __name__ == "__main__":
    s = my_stack()
    s.push("google.com")
    s.push("pynative.com")
    print(s.peek())
    print(s.pop())
    print(s.peek())
