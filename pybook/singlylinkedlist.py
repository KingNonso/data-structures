class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        # Encapsulate the data in a Node
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

        # if self.tail == None:
        #     self.tail = node
        # else:
        #     current = self.tail
        #     while current.next:
        #         current = current.next
        #     current.next = node

    # def size(self):
    #     count = 0
    #     current = self.tail
    #     while current:
    #         count += 1
    #         current = current.next
    #     return count

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        ''' Clear the entire list '''
        self.tail = None
        self.head = None


words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

for word in words.iter():
    print(word)
