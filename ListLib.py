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
            return current
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

    def Compare(self, Arg1, Arg2):
        if Arg1.how_year() > Arg2.how_year():
            return 1
        else:
            return 0

    def Sort(self):
        for i in range(self.length-1):
            for j in range(0, self.length-i-1):
                tmp_el = self.GetByID(j)
                tmp_min = None
                if self.Compare(tmp_el.value, self.GetByID(j+1).value):
                    tmp_min = self.GetByID(j+1)
                    tmp_el.prev.next = tmp_min
                    tmp_min.next.prev = tmp_el
                    tmp_el.next = tmp_min.next
                    tmp_min.prev = tmp_el.prev
                    tmp_el.prev = tmp_min
                    tmp_min.next = tmp_el

                if tmp_el == self.head:
                    self.head = tmp_min

    def clear(self):
        self.__init__()
