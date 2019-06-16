from unittest import TestCase
import OOPserv
import filecmp
import os


class TestServer(TestCase):
    def setUp(self):
        self.c = OOPserv.Container()
        self.c.Input("input.txt")

        self.oop = OOPserv.OOPlang()
        self.oop.inher = '2'
        self.oop.mentions = '12341'
        self.oop.year = '1998'

        self.prc = OOPserv.ProcLang()
        self.prc.abstract = '1'
        self.prc.mentions = '12010'
        self.prc.year = '1997'

        self.fnc = OOPserv.FuncLang()
        self.fnc.type = '1'
        self.fnc.lazy = '0'
        self.fnc.mentions = '120123'
        self.fnc.year = '1999'

        self.lang = OOPserv.Language()

    def test_ClearFile(self):
        self.c.Clear_File("output.txt")
        self.assertFalse(os.stat("output.txt").st_size)

    def test_Add(self):
        self.c.Add(self.oop)
        self.c.Add(self.prc)
        self.c.Add(self.fnc)
        self.assertTrue(self.c.head.value == self.oop and self.c.head.next.value == self.prc and self.c.head.prev.value == self.fnc)

    def test_Input(self):
        mas = [self.oop, self.prc, self.fnc]
        current = self.c.head
        for i in range(3):
            if current.value != mas[i]:
                self.fail()
            current = current.next

        self.assertTrue(1)

    def test_GetByID(self):
        self.assertTrue(self.c.Get_By_ID(1).value == self.prc and self.c.Get_By_ID(0).value == self.oop and self.c.Get_By_ID(2).value == self.fnc)

    def test_Output(self):
        self.c.Clear_File("output.txt")
        self.c.Output("output.txt")
        self.c.Sort()
        self.c.Output("output.txt")
        self.c.Output_Filter("output.txt")
        self.assertTrue(filecmp.cmp("output.txt", "outputG.txt"))

    def test_Sort(self):
        self.c.Sort()
        current = self.c.head
        mas = [self.fnc, self.oop, self.prc]
        for i in range(3):
            if current.value != mas[i]:
                self.fail()
            current = current.next
        self.assertTrue(1)

    def test_Clear(self):
        self.c.Clear("output.txt")
        self.assertTrue(self.c.head is None)

    def test_How_Year(self):
        self.lang.year = 1997
        self.assertTrue(self.lang.How_Year() == 22)

    def test_Compare(self):
        self.assertTrue(self.lang.Compare(self.oop, self.fnc))


