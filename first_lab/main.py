from place import PlaceMaster
import typer

app = typer.Typer()


class Error(Exception):
    def __init__(self, text):
        self.txt = text


@app.command()
def file(filename: str):
    while True:
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
        if enter == 'exit':
            exit(0)
        if enter == 'next':
            meadow.tick()
            move_count += 1

@app.command()
def keyboard(x_size: int, y_size: int, r: int, d: int, s: int, w: int, b: int, p: int):
    try:
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

    meadow = PlaceMaster(x_size, y_size)

    meadow.start_random_place(r, d, s, w, b, p)
    meadow.show()
    move_count = 0

    while True:
        print('Move #', move_count)
        enter = input()
        if enter == 'exit':
            exit(0)
        if enter == 'next':
            meadow.tick()
            move_count += 1

@app.command()
def preset():
    x_size = 14
    y_size = 5
    r = 5
    d = 3
    s = 3
    w = 3
    b = 3
    p = 10

    meadow = PlaceMaster(x_size, y_size)

    meadow.start_random_place(r, d, s, w, b, p)
    meadow.show()
    move_count = 0

    while True:
        print('Move #', move_count)

        enter = input()
        if enter == 'exit':
            exit(0)
        if enter == 'next':
            meadow.tick()
            move_count += 1


if __name__ == "__main__":
    app()