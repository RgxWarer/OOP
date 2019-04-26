import abc
import os
from multipledispatch import dispatch


class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class Container:
    def __init__(self):
        self.head = None
        self.length = 0

    def GetByID(self, key):
        if self.head is not None:
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

    def Input(self, input_name):
        try:
            file = open(input_name)

        except OSError:
            print("File not found")
            return 0

        if os.stat(input_name).st_size == 0:
            print("File is empty!")
            return 0

        lang = Language()
        for line in file:
            lang.Input_Lang(self, line.strip(), file.readline().split(" "))

    def Output(self, file_name):

        output_file = open(file_name, 'w')
        if self.length > 0:
            output_file.write("Number of elements = " + str(self.length) + " \n")
            current = self.head
            for i in range(self.length):
                output_file.write(str(i + 1))
                current.value.Output_Lang(output_file)
                current = current.next
            return 1
        else:
            output_file.write("No elements! \n")
            return 0

    def MultiOutput(self, file_name):

        output_file = open(file_name, 'w')
        if self.length > 0:
            for i in range(self.length - 1):
                for j in range(i+1, self.length):
                    obj1 = self.GetByID(i).value
                    obj2 = self.GetByID(j).value
                    obj1.MultiMethod(obj2, output_file)
                    obj1.Output_Lang(output_file)
                    obj2.Output_Lang(output_file)
            return 1
        else:
            output_file.write("No elements! \n")
            return 0

    def Clear(self, file_name):
        self.__init__()
        output_file = open(file_name, 'a')
        output_file.write("\nList empty. Number of elements = " + str(self.length) + " \n")


class Language:
    lang_list = Container()

    def __init__(self):
        self.year = 0  # общее поле - год разработки

    @abc.abstractmethod  # определим метод позже
    def Output_Lang(self, output_stream):
        pass

    @abc.abstractmethod  # определим метод позже
    def MultiMethod(self, obj2, output_stream):
        pass

    @abc.abstractmethod  # определим метод позже
    def MMProc(self, output_stream):
        pass

    @abc.abstractmethod  # определим метод позже
    def MMOop(self, output_stream):
        pass

    def Input_Lang(self, lang_list, lang_type, lang_params):
        if int(lang_type) == 1:  # ООП
            tmp_OOP = OOPlang()
            tmp_OOP.Input_Langs(lang_params, lang_list)
        elif int(lang_type) == 2:  # процедурный
            tmp_Proc = ProcLang()
            tmp_Proc.Input_Langs(lang_params, lang_list)
        else:
            print("Verify that the input is correct.")


class OOPlang(Language):
    def __init__(self):
        super().__init__()

    def Input_Langs(self, line, lang_list):
        self.inher, self.year = line
        lang_list.Add(self)

    def Output_Lang(self, output_stream):  # Вывод значений полей
        output_stream.write(": OOP language" + "\n" +
                            "inheritance = " + self.inher + ", year = " + self.year + "\n")

    def MultiMethod(self, obj2, output_stream):
        obj2.MMOop(output_stream)

    def MMOop(self, output_stream):
        output_stream.write("\nOOP and OOP \n")

    def MMProc(self, output_stream):
        output_stream.write("\nPROC and OOP\n")

class ProcLang(Language):
    def __init__(self):
        super().__init__()

    def Input_Langs(self, line, lang_list):
        self.abstract, self.year = line
        lang_list.Add(self)

    def Output_Lang(self, output_stream):
        output_stream.write(": Procedure language" + "\n" +
                            "abstract = " + self.abstract + ", year = " + self.year + "\n")

    def MultiMethod(self, obj2, output_stream):
        obj2.MMProc(output_stream)

    def MMProc(self, output_stream):
        output_stream.write("\nProc and Proc\n")

    def MMOop(self, output_stream):
        output_stream.write("\nOOP and PROC\n")

