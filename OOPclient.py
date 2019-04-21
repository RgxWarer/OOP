import sys
from OOPserv import Container


class Main:
    def start(self):
        if len(sys.argv) != 3:
            return print("You have not entered necessary arguments.")

        input_name = sys.argv[1]
        output_name = sys.argv[2]

        c = Container()
        c.Clear_File(output_name)
        if c.Input(input_name) != 0:
            if c.Output(output_name) != 0:
                c.Sort()
                c.Output(output_name)
                c.OutputFilter(output_name)
                c.Clear(output_name)


if __name__ == '__main__':
    print("START")
    m = Main()
    m.start()
    print("STOP")
