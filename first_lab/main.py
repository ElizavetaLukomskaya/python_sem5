from place import PlaceMaster
import typer

app = typer.Typer()

class Error(Exception):
    def __init__(self, text):
        self.txt = text

@app.command()
def main():
    x_size = 14
    y_size = 5
    r = 5
    d = 3
    s = 3
    w = 3
    b = 3
    p = 10

    print(40*'-')
    print('\nUse file\t\t---> TAB\n')
    print(40*'-')
    print('\nUse keyboard\t\t---> SPACE\n')
    print(40*'-')
    print('\nUse preset(14x5)\t---> ENTER\n')
    print(40*'-')

    enter = input()

    if enter == ' ':
        try:
            print('Enter the game table size (AxB): ')
            x_size = int(input())
            y_size = int(input())
            print('Enter organism numbers (R -> D -> S -> W -> B -> P): ')
            r = int(input())
            d = int(input())
            s = int(input())
            w = int(input())
            b = int(input())
            p = int(input())
            if r + d + s + w + b + p > x_size*y_size*4 or p > x_size * y_size:
                raise Error('Too many organisms, using default positioning instead!\n')
        except ValueError:
            print('Error type of value')
        except Error as er:
            print(er)
            x_size = 14
            y_size = 5
            r = 5
            d = 3
            s = 3
            w = 3
            b = 3
            p = 10
            input()

    if enter == '\011':
        data = []
        filename = str()
        while True:
            print('Enter filename:')
            filename = input()
            try:
                f = open(filename, 'r')
                x_size = int(f.readline())
                y_size = int(f.readline())
                r = int(f.readline())
                d = int(f.readline())
                s = int(f.readline())
                w = int(f.readline())
                b = int(f.readline())
                p = int(f.readline())
                break
            except FileNotFoundError:
                print('The file is not found')
            except ValueError:
                print('Error type of value')


    meadow = PlaceMaster(x_size, y_size)

    meadow.start_random_place(r, d, s, w, b, p)
    meadow.show()
    move_count = 0

    while True:
        print('Move #', move_count)

        enter = input()
        if enter == 'q':
            exit(0)
        if enter == 'z':
            meadow.tick()
            move_count += 1

if __name__ == "__main__":
    app()