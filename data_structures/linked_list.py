import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.end = new_node
            return

        self.end.next = new_node
        self.end = new_node

        # current_node = self.head
        # while current_node.next:
        #     current_node = current_node.next
        # current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' => ' if current_node.next else '\n')
            current_node = current_node.next


linked_lst = LinkedList()
linked_lst.append(123)
linked_lst.append([1, 2, 3])
linked_lst.append("123")
linked_lst.prepend('first')
linked_lst.print_list()

n = 100000

lst = []
start = time.time()
for i in range(n):
    lst.append(i)
end = time.time()
print(end - start)  # 0.008526802062988281

lst = []
start = time.time()
for i in range(n):
    lst.insert(0, i)
end = time.time()
print(end - start)  # 2.131622791290283

linked_1st = LinkedList()
start = time.time()
for i in range(n):
    linked_1st.append(i)
end = time.time()
print(end - start)  # 0.05362439155578613

linked_1st = LinkedList()
start = time.time()
for i in range(n):
    linked_1st.prepend(i)
end = time.time()
print(end - start)  # 0.05108761787414551
