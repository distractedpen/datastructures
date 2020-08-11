#queue implementation

class Queue():

    def __init__(self, MAXSIZE):
        self.q = [0] * MAXSIZE
        self.MAXSIZE = MAXSIZE
        self.front = 0
        self.rear = -1
        self.itemCount = 0

    def peek(self):
        return self.q[self.front]

    def isFull(self):
        return self.itemCount == self.MAXSIZE

    def isEmpty(self):
        return self.itemCount == 0

    def enqueue(self, data):
        if self.isFull():
            return 0
        else:
            if self.rear == (self.MAXSIZE - 1):
                self.rear = -1
            self.rear += 1
            self.q[self.rear] = data
            self.itemCount += 1

    def dequeue(self):
        if self.isEmpty():
            return "Error"
        else:
            if self.front == self.MAXSIZE:
                self.front = 0
            data = self.q[self.front]
            self.front += 1
            self.itemCount -= 1
            return data

    def debug(self):
        print("Front: {0}".format(self.front))
        print("Rear: {0}".format(self.rear))
        print("Queue: {0}".format(self.q))


def main():
    q = Queue(5)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while(not q.isEmpty()):
        print(q.dequeue(), end=" ")
    print("\n")


    i = 10
    while(not q.isFull()):
        q.enqueue(i)
        i += 1


    while(not q.isEmpty()):
        print(q.dequeue(), end=" ")

if __name__ == "__main__":
    main()
        
