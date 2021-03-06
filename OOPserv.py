import datetime
import abc
import os


class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class Container:
    def __init__(self):
        self.head = None
        self.length = 0

    def Get_By_ID(self, key):
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
            if line:
                lang.Input_Lang(self, line.strip(), file.readline().strip().split(" "))
        file.close()

    def Output(self, file_name):

        output_file = open(file_name, 'a')
        if self.length > 0:
            output_file.write("\nNumber of elements = " + str(self.length) + " \n")
            current = self.head
            for i in range(self.length):
                output_file.write(str(i + 1))
                current.value.Output_Lang(output_file)
                current = current.next
            output_file.close()
            return 1
        else:
            output_file.write("No elements! \n\n")
            output_file.close()
            return 0

    def Output_Filter(self, file_name):

        output_file = open(file_name, 'a')
        if self.length > 0:
            output_file.write("\nNumber of elements = " + str(self.length) + " \n")
            current = self.head
            for i in range(self.length):
                output_file.write(str(i + 1))
                current.value.Output_Lang_Filter(output_file)
                current = current.next
            output_file.close()
            return 1
        else:
            output_file.write("No elements! \n\n")
            output_file.close()
            return 0

    def Sort(self):
        lang = Language()
        for i in range(self.length - 1):
            for j in range(0, self.length - i - 1):
                tmp_el = self.Get_By_ID(j)
                tmp_min = None
                if lang.Compare(tmp_el.value, self.Get_By_ID(j + 1).value):
                    tmp_min = self.Get_By_ID(j + 1)
                    tmp_el.prev.next = tmp_min
                    tmp_min.next.prev = tmp_el
                    tmp_el.next = tmp_min.next
                    tmp_min.prev = tmp_el.prev
                    tmp_el.prev = tmp_min
                    tmp_min.next = tmp_el
                    if tmp_el == self.head:
                        self.head = tmp_min

    def Clear(self, file_name):
        self.__init__()
        output_file = open(file_name, 'a')
        output_file.write("\nList empty. Number of elements = " + str(self.length) + " \n")
        output_file.close()

    def Clear_File(self, file_name):
        open(file_name, 'w').close()


class Language:
    lang_list = Container()

    def __init__(self):
        self.year = 0  # общее поле - год разработки
        self.mentions = 0  # общее поле - упоминания
        self.oop_txt = {0: "single",
                        1: "multiply",
                        2: "interface"}
        self.bool_txt = {0: "no",
                         1: "yes"}
        self.func_txt = {0: "strong",
                         1: "dynamic"}

    @abc.abstractmethod  # определим метод позже
    def Output_Lang(self, output_stream):
        pass

    def Output_Lang_Filter(self, output_stream):
        output_stream.write(". \n\n")


    def Input_Lang(self, lang_list, lang_type, lang_params):
        if lang_type == "1":  # ООП
            tmp_oop = OOPlang()
            tmp_oop.Input_Langs(lang_params, lang_list)
        elif lang_type == "2":  # процедурный
            tmp_proc = ProcLang()
            tmp_proc.Input_Langs(lang_params, lang_list)
        elif lang_type == "3":  # функциональный
            tmp_func = FuncLang()
            tmp_func.Input_Langs(lang_params, lang_list)
        else:
            print("Verify that the input is correct.")

    def How_Year(self):
        return datetime.datetime.now().year - int(self.year)

    def Compare(self, arg1, arg2):
        if arg1.How_Year() > arg2.How_Year():
            return 1
        else:
            return 0


class OOPlang(Language):
    def __init__(self):
        super().__init__()

    def __eq__(self, other):
        if isinstance(other, OOPlang):
            return (self.inher == other.inher and
                    self.mentions == other.mentions and
                    self.year == other.year)
        return NotImplemented


    def Input_Langs(self, line, lang_list):
        try:
            self.inher, self.mentions, self.year = line
            try:
                temp1 = self.oop_txt[int(self.inher)]
                temp2 = int(self.mentions)
                temp3 = int(self.year)

                lang_list.Add(self)
            except:
                print("Verify that the all parameters is correct.")
        except:
            print("Verify that the number of parameters is correct.")

    def Output_Lang(self, output_stream):
        output_stream.write(". OOP language: " + "inheritance = " + self.oop_txt[int(self.inher)] + ", number of mentions = " +
                            self.mentions + ", year = " + self.year + ", how old = " + str(self.How_Year()) + "\n")


class ProcLang(Language):
    def __init__(self):
        super().__init__()

    def __eq__(self, other):
        if isinstance(other, ProcLang):
            return (self.abstract == other.abstract and
                    self.mentions == other.mentions and
                    self.year == other.year)
        return NotImplemented

    def Input_Langs(self, line, lang_list):
        try:
            self.abstract, self.mentions, self.year = line
            try:
                temp1 = self.bool_txt[int(self.abstract)]
                temp2 = int(self.mentions)
                temp2 = int(self.year)
                lang_list.Add(self)
            except:
                print("Verify that the all parameters is correct.")
        except:
            print("Verify that the number of parameters is correct.")


    def Output_Lang(self, output_stream):  # Вывод значений полей
        output_stream.write(". Procedure language: " + "abstract = " + self.bool_txt[int(self.abstract)] + ", number of mentions = " +
                            self.mentions + ", year = " + self.year + ", how old = " + str(self.How_Year()) + "\n")

    def Output_Lang_Filter(self, output_stream):  # Вывод значений полей
        self.Output_Lang(output_stream)


class FuncLang(Language):
    def __init__(self):
        super().__init__()

    def __eq__(self, other):
        if isinstance(other, FuncLang):
            return (self.type == other.type and
                    self.lazy == other.lazy and
                    self.mentions == other.mentions and
                    self.year == other.year)
        return NotImplemented

    def Input_Langs(self, line, lang_list):
        try:
            self.type, self.lazy, self.mentions, self.year = line
            try:
                temp1 = self.func_txt[int(self.type)]
                temp2 = self.bool_txt[int(self.lazy)]
                temp2 = int(self.mentions)
                temp2 = int(self.year)
                lang_list.Add(self)
            except:
                print("Verify that the all parameters is correct.")
        except:
            print("Verify that the number of parameters is correct.")

    def Output_Lang(self, output_stream):
        output_stream.write(". Functional language: " + "typification = " + self.func_txt[int(self.type)] +
                            ", lazy computing support = " + self.bool_txt[int(self.lazy)] + ", number of mentions = " + self.mentions
                            + ", year = " + self.year + ", how old = " + str(self.How_Year()) + "\n")






