class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            self.show_error("Error: La cola está vacía")

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            self.show_error("Error: La cola está vacía")

    def show_error(self, message):
        raise ValueError(message)
