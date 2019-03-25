# класс Node для определения элемента списка
class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class List:
    def __init__(self):
        self.head = None
        self.length = 0

    def GetByID(self, key):
        if self.head != None:
            current = self.head
            for k in range(key):
                if self.head != current.next:
                    current = current.next
                else:
                    return "Out of range"
            return current.value
        return 'Empty List'

    def Add(self, x):
        self.length += 1
        if self.head is None:
            self.head = Node(x, None, None)
            self.head.next = self.head.prev = self.head

        else:
            new_link = Node(x, None, None)
            last = self.head.prev
            self.head.prev = last.next = new_link
            new_link.prev = last
            new_link.next = self.head

    def Sort(self):

        for i in range(self.length):
            for j in range(1, self.length - i - 1):
                if self.GetByID(i).how_year() > self.GetByID(j).how_year():



    def clear(self):
        self.__init__()
