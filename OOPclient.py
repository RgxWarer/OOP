import sys
from OOPserv import Container


class Main:
    def start(self):
        if len(sys.argv) != 3:
            return print("You have not entered necessary arguments.")

        input_name = sys.argv[1]
        output_name = sys.argv[2]

        c = Container()
        if c.Input(input_name) != 0:
            c.Sort()
            if c.Output(output_name) != 0:
                c.Clear(output_name)


if __name__ == '__main__':
    print("START")
    m = Main()
    m.start()
    print("STOP")
