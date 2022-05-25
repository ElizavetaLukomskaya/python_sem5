from place import PlaceMaster
from animals import Rabbit, Deer, Squirrel, Wolf, Bear, Plant
import typer
import json
import datetime
import pygame
import random
from os import path
from plain import *

app = typer.Typer()


class Error(Exception):
    def __init__(self, text):
        self.txt = text


def save(data):
    print("Write name of file to save: ")
    filename = str(input())

    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

@app.command()
def load(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        for p in data['Matrix']:
            x_size = p['x_size']
            y_size = p['y_size']

        meadow = PlaceMaster(x_size, y_size)

        for p in data['Rabbit']:
            if p['male'] == True:
                org_rab_obj = Rabbit('Male')
            else:
                org_rab_obj = Rabbit('Female')
            coordinates = p['coordinates']
            org_rab_obj.location0 = coordinates[0]
            org_rab_obj.location1 = coordinates[1]
            org_rab_obj.location2 = coordinates[2]
            org_rab_obj.hp = p['hp']
            org_rab_obj.food = p['food']
            org_rab_obj.age = p['age']
            meadow.org_rabbit.append(org_rab_obj)

        for p in data['Deer']:
            if p['male'] == True:
                org_deer_obj = Deer('Male')
            else:
                org_deer_obj = Deer('Female')
            coordinates = p['coordinates']
            org_deer_obj.location0 = coordinates[0]
            org_deer_obj.location1 = coordinates[1]
            org_deer_obj.location2 = coordinates[2]
            org_deer_obj.hp = p['hp']
            org_deer_obj.food = p['food']
            org_deer_obj.age = p['age']
            meadow.org_deer.append(org_deer_obj)

        for p in data['Squirrel']:
            if p['male'] == True:
                org_sq_obj = Squirrel('Male')
            else:
                org_sq_obj = Squirrel('Female')
            coordinates = p['coordinates']
            org_sq_obj.location0 = coordinates[0]
            org_sq_obj.location1 = coordinates[1]
            org_sq_obj.location2 = coordinates[2]
            org_sq_obj.hp = p['hp']
            org_sq_obj.food = p['food']
            org_sq_obj.age = p['age']
            meadow.org_squirrel.append(org_sq_obj)

        for p in data['Wolf']:
            if p['male'] == True:
                org_wolf_obj = Wolf('Male')
            else:
                org_wolf_obj = Wolf('Female')
            coordinates = p['coordinates']
            org_wolf_obj.location0 = coordinates[0]
            org_wolf_obj.location1 = coordinates[1]
            org_wolf_obj.location2 = coordinates[2]
            org_wolf_obj.hp = p['hp']
            org_wolf_obj.food = p['food']
            org_wolf_obj.age = p['age']
            meadow.org_wolf.append(org_wolf_obj)

        for p in data['Bear']:
            if p['male'] == True:
                org_b_obj = Bear('Male')
            else:
                org_b_obj = Bear('Female')
            coordinates = p['coordinates']
            org_b_obj.location0 = coordinates[0]
            org_b_obj.location1 = coordinates[1]
            org_b_obj.location2 = coordinates[2]
            org_b_obj.hp = p['hp']
            org_b_obj.food = p['food']
            org_b_obj.age = p['age']
            meadow.org_bear.append(org_b_obj)

        for p in data['Plant']:
            org_pl_obj = Plant()
            coordinates = p['coordinates']
            org_pl_obj.location0 = coordinates[0]
            org_pl_obj.location1 = coordinates[1]
            org_pl_obj.location2 = coordinates[2]
            org_pl_obj.hp = p['hp']
            org_pl_obj.age = p['age']
            meadow.org_plant.append(org_pl_obj)


        meadow.update_map()
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

def convert_to_data(x_size: int, y_size: int, r, d, s, w, b, p, date):

    data = {}
    data['Date'] = date
    data['Matrix'] = []
    data['Rabbit'] = []
    data['Deer'] = []
    data['Squirrel'] = []
    data['Wolf'] = []
    data['Bear'] = []
    data['Plant'] = []
    data['Matrix'].append({
        'x_size': x_size,
        'y_size': y_size,
        'rabbit_number': len(r),
        'deer_number': len(d),
        'squirrel_number': len(s),
        'wolf_number': len(w),
        'bear_number': len(b),
        'plant_number': len(p),
                      })

    for i in range(len(r)):
        data['Rabbit'].append({
            'number': i,
            'male': r[i].is_male,
            'coordinates': [r[i].location0, r[i].location1, r[i].location2],
            'hp': r[i].hp,
            'food': r[i].food,
            'age': r[i].age
    })

    for i in range(len(d)):
        data['Deer'].append({
            'number': i,
            'male': d[i].is_male,
            'coordinates': [d[i].location0, d[i].location1, d[i].location2],
            'hp': d[i].hp,
            'food': d[i].food,
            'age': d[i].age
    })

    for i in range(len(s)):
        data['Squirrel'].append({
            'number': i,
            'male': s[i].is_male,
            'coordinates': [s[i].location0, s[i].location1, s[i].location2],
            'hp': s[i].hp,
            'food': s[i].food,
            'age': s[i].age
    })

    for i in range(len(w)):
        data['Wolf'].append({
            'number': i,
            'male': w[i].is_male,
            'coordinates': [w[i].location0, w[i].location1, w[i].location2],
            'hp': w[i].hp,
            'food': w[i].food,
            'age': w[i].age
    })

    for i in range(len(b)):
        data['Bear'].append({
            'number': i,
            'male': b[i].is_male,
            'coordinates': [b[i].location0, b[i].location1, b[i].location2],
            'hp': b[i].hp,
            'food': b[i].food,
            'age':b[i].age
    })

    for i in range(len(p)):
        data['Plant'].append({
            'number': i,
            'coordinates': [p[i].location0, p[i].location1, p[i].location2],
            'hp': p[i].hp,
            'age': p[i].age
    })

    return data

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
        if enter == 'save':
            date = str(datetime.datetime.now())
            save(convert_to_data(x_size, y_size, meadow.org_rabbit, meadow.org_deer, meadow.org_squirrel, meadow.org_wolf, meadow.org_bear, meadow.org_plant, date))
            exit(0)
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

@app.command()
def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LAB4")

    bg = pygame.image.load("grass.png")
    bg = pygame.transform.scale(bg, (1700, 1200))

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    #max_x_for_plain = 19
    #max_y_dor_plain = 12

    x_p = 19
    y_p = 12

    pl = Plain(x_p, y_p)
    all_sprites.add(pl)

    an = []

    #max_x_for_animals = max_x_for_plain - 1
    #max_y_dor_animals = max_y_for_plain - 1

    an.append(Animal(0, 0, 0, 'p', pl))
    an.append(Animal(0, 1, 0, 'p', pl))
    an.append(Animal(0, 2, 0, 'p', pl))
    an.append(Animal(0, 3, 0, 'p', pl))
    an.append(Animal(0, 4, 0, 'p', pl))
    an.append(Animal(0, 5, 0, 'p', pl))

    an.append(Animal(0, 6, 0, 'p', pl))
    an.append(Animal(0, 7, 0, 'p', pl))
    an.append(Animal(0, 8, 0, 'p', pl))
    an.append(Animal(0, 9, 0, 'p', pl))
    an.append(Animal(0, 10, 0, 'p', pl))
    an.append(Animal(0, 11, 0, 'p', pl))



    an.append(Animal(2, 6, 3, 'r', pl))
    an.append(Animal(3, 7, 3, 'r', pl, sex='Female'))
    an.append(Animal(4, 6, 2, 's', pl))
    an.append(Animal(3, 10, 2, 's', pl, sex='Male'))
    an.append(Animal(5, 6, 2, 'w', pl))
    an.append(Animal(6, 10, 2, 'w', pl, sex='Female'))
    an.append(Animal(7, 6, 2, 'd', pl))
    an.append(Animal(8, 11, 2, 'd', pl, sex='Female'))
    an.append(Animal(9, 6, 2, 'b', pl))
    an.append(Animal(18, 11, 3, 'b', pl, sex='Female'))

    all_sprites.add(an)

    running = True

    while running:
        clock.tick(60)

        screen.blit(bg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i in range(len(an)):
            an[i].animate()

        all_sprites.update()


        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    app()