from collections import deque
class Q:
    def __init__(self) -> None:
        self.q = deque()
    def enqueue(self, e):
        self.q.append(e)
    def dequeue(self):
        return self.q.popleft()
    def peek(self):
        return self.q[0]
if __name__ == "__main__":
    my_queue = Q()
    my_queue.enqueue("Customer A")
    my_queue.enqueue("Customer B")
    print(my_queue.dequeue())
    print(my_queue.peek())
