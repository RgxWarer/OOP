from ListLib import List
import abc
import os
import datetime


class Container:
    def __init__(self):
        self.lang_list = List()

    def input_lang(self, input_name):
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
            lang.input_lang(self.lang_list, line, file.readline().split(" "))

    def output_lang(self, file_name):

        output_file = open(file_name, 'w')
        if self.lang_list.length > 0:
            self.lang_list.Sort()
            output_file.write("Number of elements = " + str(self.lang_list.length) + " \n")

            for i in range(self.lang_list.length):
                lang = self.lang_list.GetByID(i).value
                output_file.write(str(i + 1))
                lang.output_lang(output_file)
            return 1
        else:
            output_file.write("No elements! \n")
            return 0

    def clear_list(self, file_name):
        self.lang_list.clear()
        output_file = open(file_name, 'a')
        output_file.write("\nList empty. Number of elements = " + str(self.lang_list.length) + " \n")


class Language:
    lang_list = List()

    def __init__(self):
        self.year = 0  # общее поле - год разработки

    @abc.abstractmethod  # определим метод позже
    def output_lang(self, output_stream):
        pass

    def input_lang(self, lang_list, lang_type, lang_params):
        if int(lang_type) == 1:  # ООП
            tmp_OOP = OOPlang()
            tmp_OOP.input_langs(lang_params, lang_list)
        elif int(lang_type) == 2:  # процедурный
            tmp_Proc = ProcLang()
            tmp_Proc.input_langs(lang_params, lang_list)
        else:
            print("Verify that the input is correct.")

    def how_year(self):
        return datetime.datetime.now().year - int(self.year)


class OOPlang(Language):
    def __init__(self):
        super().__init__()

    def input_langs(self, line, lang_list):
        self.inher, self.year = line
        lang_list.Add(self)

    def output_lang(self, output_stream):  # Вывод значений полей
        output_stream.write(": OOP language" + "\n" + "inheritance = " + self.inher + ", year = " +
                            self.year.strip() + ", how old: " + str(self.how_year()) + "\n")


class ProcLang(Language):
    def __init__(self):
        super().__init__()

    def input_langs(self, line, lang_list):
        self.abstract, self.year = line
        lang_list.Add(self)

    def output_lang(self, output_stream):
        output_stream.write(": Procedure language" + "\n" + "abstract = " + self.abstract + ", year = " +
                            self.year.strip() + ", how old: " + str(self.how_year()) + "\n")
