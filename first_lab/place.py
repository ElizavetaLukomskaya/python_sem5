# Class about Field
import random
from animals import Plant, Predator, Bear, Wolf, Victim, Rabbit, Deer, Squirrel


class PlaceField(object):
    # Constructor of Meadowfield
    def __init__(self, width, height):
        self._width = width
        self._height = height

        self.scene = []
        for i in range(self._width):
            self.scene_2 = []
            for j in range(self._height):
                self.scene_3 = []
                for k in range(4):
                    self.scene_3.append(' ')
                self.scene_2.append(self.scene_3)
            self.scene.append(self.scene_2)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    # Printing the Meadowfield Layout
    def display_scene(self):
        print()
        print("\t\t\tFOREST\n")
        st = "   "
        for i in range(self._width):
            st = st + "     " + str(i + 1)
        print(st)

        for r in range(self._height):
            st = "     "
            if r == 0:
                for col in range(self._width):
                    st = st + "|_____"
                print(st + "|")

            st = "     "
            for col in range(self._width):
                st = st + "| " + str(self.scene[col][r][0]) + " " + str(self.scene[col][r][1]) + " "
            print(st + "|")

            st = "  " + str(r + 1) + "  "
            for col in range(self._width):
                st = st + "| " + str(self.scene[col][r][2]) + " " + str(self.scene[col][r][3]) + " "
            print(st + "|")

            st = "     "
            for col in range(self._width):
                st = st + "|_____"
            print(st + '|')

        print()

    # Function for setting up Organisms
    def put_org(self, pos_x, pos_y, pos_i, org_type):
        self.scene[pos_x][pos_y][pos_i] = org_type

    # Find empty cell of Meadowfield
    def find_empty_cell(self, is_plant):
        i = random.randint(0, self._width - 1)
        j = random.randint(0, self._height - 1)
        k = 0
        variations = 0
        coords = [0, 0, 0]

        while self.scene[i][j][k] != ' ' and variations < self._width * self._height:
            for c in range(4):
                if is_plant:
                    if self.scene[i][j][c] == 'p':
                        break
                if self.scene[i][j][c] == ' ':
                    coords[0] = i
                    coords[1] = j
                    coords[2] = c
                    return coords

            i = random.randint(0, self._width - 1)
            j = random.randint(0, self._height - 1)
            variations += 1

        if variations < self._width * self._height:
            coords[0] = i
            coords[1] = j
            coords[2] = k
            return coords

        coords[0] = -1
        coords[1] = -1
        coords[2] = -1
        return coords


class PlaceMaster(object):
    # Constructor of PlaceMaster
    def __init__(self, width_inp: int, height_inp: int):
        self.meadow_table = PlaceField(width_inp, height_inp)
        self.rabbit_number = 0
        self.deer_number = 0
        self.squirrel_number = 0
        self.wolf_number = 0
        self.bear_number = 0
        self.plant_number = 0

        self.org_rabbit = []
        self.org_deer = []
        self.org_squirrel = []
        self.org_wolf = []
        self.org_bear = []
        self.org_plant = []

        self.p_extra = Plant()
        self.d_extra = Deer('Random')
        self.r_extra = Rabbit('Random')
        self.s_extra = Squirrel('Random')


    # Update MeadowField after changes
    def update_map(self):
        for i in range(self.meadow_table.width):
            for j in range(self.meadow_table.height):
                for k in range(4):
                    self.meadow_table.scene[i][j][k] = ' '

        for i in range(len(self.org_rabbit)):
            self.meadow_table.scene[self.org_rabbit[i].location0][self.org_rabbit[i].location1][self.org_rabbit[i].location2] = 'R'
        for i in range(len(self.org_deer)):
            self.meadow_table.scene[self.org_deer[i].location0][self.org_deer[i].location1][self.org_deer[i].location2] = 'D'
        for i in range(len(self.org_squirrel)):
            self.meadow_table.scene[self.org_squirrel[i].location0][self.org_squirrel[i].location1][self.org_squirrel[i].location2] = 'S'
        for i in range(len(self.org_wolf)):
            self.meadow_table.scene[self.org_wolf[i].location0][self.org_wolf[i].location1][self.org_wolf[i].location2] = 'W'
        for i in range(len(self.org_bear)):
            self.meadow_table.scene[self.org_bear[i].location0][self.org_bear[i].location1][self.org_bear[i].location2] = 'B'
        for i in range(len(self.org_plant)):
            self.meadow_table.scene[self.org_plant[i].location0][self.org_plant[i].location1][self.org_plant[i].location2] = 'P'

    # Get start positions
    def start_random_place(self, r_c, d_c, s_c, w_c, b_c, p_c):
        for i in range(r_c):
            if i%2 != 0:
                self.org_rabbit_obj = Rabbit('Male')
                self.org_rabbit_obj._id = self.rabbit_number
                self.org_rabbit.append(self.org_rabbit_obj)
            else:
                self.org_rabbit_obj = Rabbit('Female')
                self.org_rabbit_obj._id = self.rabbit_number
                self.org_rabbit.append(self.org_rabbit_obj)

            self.rabbit_number += 1

        for i in range(d_c):
            if i % 2 != 0:
                self.org_deer_obj = Deer('Male')
                self.org_deer_obj._id = self.deer_number
                self.org_deer.append(self.org_deer_obj)
            else:
                self.org_deer_obj = Deer('Female')
                self.org_deer_obj._id = self.deer_number
                self.org_deer.append(self.org_deer_obj)

            self.deer_number += 1

        for i in range(s_c):
            if i % 2 != 0:
                self.org_squirrel_obj = Squirrel('Male')
                self.org_squirrel_obj._id = self.squirrel_number
                self.org_squirrel.append(self.org_squirrel_obj)
            else:
                self.org_squirrel_obj = Squirrel('Female')
                self.org_squirrel_obj._id = self.squirrel_number
                self.org_squirrel.append(self.org_squirrel_obj)

            self.squirrel_number += 1

        for i in range(w_c):
            if i % 2 != 0:
                self.org_wolf_obj = Wolf('Male')
                self.org_wolf_obj._id = self.wolf_number
                self.org_wolf.append(self.org_wolf_obj)
            else:
                self.org_wolf_obj = Wolf('Female')
                self.org_wolf_obj._id = self.wolf_number
                self.org_wolf.append(self.org_wolf_obj)

            self.wolf_number += 1

        for i in range(b_c):
            if i % 2 != 0:
                self.org_bear_obj = Bear('Male')
                self.org_bear_obj._id = self.bear_number
                self.org_bear.append(self.org_bear_obj)
            else:
                self.org_bear_obj = Bear('Female')
                self.org_bear_obj._id = self.bear_number
                self.org_bear.append(self.org_bear_obj)

            self.bear_number += 1

        for i in range(p_c):
            self.org_plant_obj = Plant()
            self.org_plant_obj._id = self.plant_number
            self.org_plant.append(self.org_plant_obj)
            self.plant_number += 1

        # start places
        for i in range(len(self.org_rabbit)):
            cell_coords = self.meadow_table.find_empty_cell(False)
            self.org_rabbit[i].location0 = cell_coords[0]
            self.org_rabbit[i].location1 = cell_coords[1]
            self.org_rabbit[i].location2 = cell_coords[2]

            self.meadow_table.put_org(cell_coords[0], cell_coords[1], cell_coords[2], 'R')

        for i in range(len(self.org_deer)):
            cell_coords = self.meadow_table.find_empty_cell(False)
            self.org_deer[i].location0 = cell_coords[0]
            self.org_deer[i].location1 = cell_coords[1]
            self.org_deer[i].location2 = cell_coords[2]

            self.meadow_table.put_org(cell_coords[0], cell_coords[1], cell_coords[2], 'D')

        for i in range(len(self.org_squirrel)):
            cell_coords = self.meadow_table.find_empty_cell(False)
            self.org_squirrel[i].location0 = cell_coords[0]
            self.org_squirrel[i].location1 = cell_coords[1]
            self.org_squirrel[i].location2 = cell_coords[2]

            self.meadow_table.put_org(cell_coords[0], cell_coords[1], cell_coords[2], 'S')

        for i in range(len(self.org_wolf)):
            cell_coords = self.meadow_table.find_empty_cell(False)
            self.org_wolf[i].location0 = cell_coords[0]
            self.org_wolf[i].location1 = cell_coords[1]
            self.org_wolf[i].location2 = cell_coords[2]

            self.meadow_table.put_org(cell_coords[0], cell_coords[1], cell_coords[2], 'W')

        for i in range(len(self.org_bear)):
            cell_coords = self.meadow_table.find_empty_cell(False)
            self.org_bear[i].location0 = cell_coords[0]
            self.org_bear[i].location1 = cell_coords[1]
            self.org_bear[i].location2 = cell_coords[2]

            self.meadow_table.put_org(cell_coords[0], cell_coords[1], cell_coords[2], 'B')

        for i in range(len(self.org_plant)):
            cell_coords = self.meadow_table.find_empty_cell(True)
            self.org_plant[i].location0 = cell_coords[0]
            self.org_plant[i].location1 = cell_coords[1]
            self.org_plant[i].location2 = cell_coords[2]

            self.meadow_table.put_org(cell_coords[0], cell_coords[1], cell_coords[2], 'P')

        self.update_map()

    def empty_place(self, x1, y1, is_plant):
        if 0 > x1 or 0 > y1 or x1 >= self.meadow_table.width or y1 >= self.meadow_table.height:
            return -1
        if is_plant:
            for i in range(len(self.org_plant)):
                if self.org_plant[i].location0 == x1 and self.org_plant[i].location1 == y1:
                    return -1
        for i in range(4):
            if self.meadow_table.scene[x1][y1][i] == ' ':
                return i
        return -1

    def plant_replicate(self, p_obj: Plant):
        x = p_obj.location0
        y = p_obj.location1
        direction = random.randint(1, 4)
        current_width = self.meadow_table.width
        current_height = self.meadow_table.height
        variations = 0
        while variations < current_width * current_height:
            if direction == 1:
                index_plant = self.empty_place(x, y-1, True)
                index = self.empty_place(x, y-1, False)
                if index_plant != -1:
                    p_child = Plant()
                    p_child.location0 = x
                    p_child.location1 = y-1
                    p_child.location2 = index_plant
                    p_child.id = self.plant_number
                    self.plant_number += 1
                    self.org_plant.append(p_child)
                    self.meadow_table.scene[p_child.location0][p_child.location1][p_child.location2] = 'P'
                    break
                if index_plant == -1 and index != -1:
                    for i in range(len(self.org_plant)):
                        if self.org_plant[i].location0 == x and self.org_plant[i].location1 == y-1:
                            self.org_plant[i].hp = self.org_plant[i].hp_max
                    break
                if index == -1:
                    direction = random.randint(1, 4)

            if direction == 2:
                index_plant = self.empty_place(x, y + 1, True)
                index = self.empty_place(x, y + 1, False)
                if index_plant != -1:
                    p_child = Plant()
                    p_child.location0 = x
                    p_child.location1 = y+1
                    p_child.location2 = index_plant
                    p_child.id = self.plant_number
                    self.plant_number += 1
                    self.org_plant.append(p_child)
                    self.meadow_table.scene[p_child.location0][p_child.location1][p_child.location2] = 'P'
                    break
                if index_plant == -1 and index != -1:
                    for i in range(len(self.org_plant)):
                        if self.org_plant[i].location0 == x and self.org_plant[i].location1 == y + 1:
                            self.org_plant[i].hp = self.org_plant[i].hp_max
                    break
                if index == -1:
                    direction = random.randint(1, 4)

            if direction == 3:
                index_plant = self.empty_place(x + 1, y, True)
                index = self.empty_place(x + 1, y, False)
                if index_plant != -1:
                    p_child = Plant()
                    p_child.location0 = x+1
                    p_child.location1 = y
                    p_child.location2 = index_plant
                    p_child.id = self.plant_number
                    self.plant_number += 1
                    self.org_plant.append(p_child)
                    self.meadow_table.scene[p_child.location0][p_child.location1][p_child.location2] = 'P'
                    break
                if index_plant == -1 and index != -1:
                    for i in range(len(self.org_plant)):
                        if self.org_plant[i].location0 == x + 1 and self.org_plant[i].location1 == y:
                            self.org_plant[i].hp = self.org_plant[i].hp_max
                    break
                if index == -1:
                    direction = random.randint(1, 4)

            if direction == 4:
                index_plant = self.empty_place(x - 1, y, True)
                index = self.empty_place(x - 1, y, False)
                if index_plant != -1:
                    p_child = Plant()
                    p_child.location0 = x-1
                    p_child.location1 = y
                    p_child.location2 = index_plant
                    p_child.id = self.plant_number
                    self.plant_number += 1
                    self.org_plant.append(p_child)
                    self.meadow_table.scene[p_child.location0][p_child.location1][p_child.location2] = 'P'
                    break
                if index_plant == -1 and index != -1:
                    for i in range(len(self.org_plant)):
                        if self.org_plant[i].location0 == x - 1 and self.org_plant[i].location1 == y:
                            self.org_plant[i].hp = self.org_plant[i].hp_max
                    break
                if index == -1:
                    direction = random.randint(1, 4)

            variations += 1

    def plant_age(self, p_obj: Plant, order):
        p_obj.age = p_obj.age + 1
        p_obj.hp = p_obj.hp - 1
        if 0 >= p_obj.hp:
            self.meadow_table.scene[p_obj.location0][p_obj.location1][p_obj.location2] = ' '
            self.org_plant.pop(order)

    def return_plant(self, x, y):
        for i in range(len(self.org_plant)):
            if self.org_plant[i].location0 == x and self.org_plant[i].location1 == y:
                return self.org_plant[i]

        self.p_extra.location0 = -1
        self.p_extra.location1 = -1
        self.p_extra.location2 = -1
        return self.p_extra

    def return_deer(self, x, y):
        for i in range(len(self.org_deer)):
            if self.org_deer[i].location0 == x and self.org_deer[i].location1 == y:
                return self.org_deer[i]

        self.d_extra.location0 = -1
        self.d_extra.location1 = -1
        self.d_extra.location2 = -1
        return self.d_extra

    def return_rabbit(self, x, y):
        for i in range(len(self.org_rabbit)):
            if self.org_rabbit[i].location0 == x and self.org_rabbit[i].location1 == y:
                return self.org_rabbit[i]

        self.r_extra.location0 = -1
        self.r_extra.location1 = -1
        self.r_extra.location2 = -1
        return self.r_extra

    def return_squirrel(self, x, y):
        for i in range(len(self.org_squirrel)):
            if self.org_squirrel[i].location0 == x and self.org_squirrel[i].location1 == y:
                return self.org_squirrel[i]

        self.s_extra.location0 = -1
        self.s_extra.location1 = -1
        self.s_extra.location2 = -1
        return self.s_extra

    def show(self):
        self.meadow_table.display_scene()

    def victim_move(self, c_obj: Victim):
        x = c_obj.location0
        y = c_obj.location1
        direction = random.randint(1, 4)
        index = 0
        variations = 0
        current_width = self.meadow_table.width
        current_height = self.meadow_table.height

        if c_obj.food <= 0.8 * c_obj.food_max:
            plant_obj = Plant()
            plant_obj = self.return_plant(x, y)
            if plant_obj.location0 == x and plant_obj.location1 == y:
                return

        while variations < current_width*current_height:
            if direction == 1:
                index = self.empty_place(x, y-1, 0)
                if index != -1:
                    c_obj.location1 = y-1
                    c_obj.location2 = index
                    break
                else:
                    direction = random.randint(1,4)

            if direction == 2:
                index = self.empty_place(x, y + 1, 0)
                if index != -1:
                    c_obj.location1 = y + 1
                    c_obj.location2 = index
                    break
                else:
                    direction = random.randint(1, 4)

            if direction == 3:
                index = self.empty_place(x + 1, y, 0)
                if index != -1:
                    c_obj.location0 = x + 1
                    c_obj.location2 = index
                    break
                else:
                    direction = random.randint(1, 4)

            if direction == 4:
                index = self.empty_place(x - 1, y, 0)
                if index != -1:
                    c_obj.location0 = x - 1
                    c_obj.location2 = index
                    break
                else:
                    direction = random.randint(1, 4)

            variations += 1

        self.meadow_table.scene[c_obj.location0][c_obj.location1][c_obj.location2] = c_obj.type

    def victim_eat(self, c_obj: Victim):
        x = c_obj.location0
        y = c_obj.location1

        if c_obj.food <= 0.7 * c_obj.food_max:
            plant_obj = self.return_plant(x, y)
            x_plant = plant_obj.location0
            y_plant = plant_obj.location1
            if x_plant == x and y_plant == y:
                c_obj.food = c_obj.food + 3 * plant_obj.hp_max
                if c_obj.food > c_obj.food_max:
                    c_obj.food = c_obj.food_max
                self.meadow_table.scene[x_plant][y_plant][plant_obj.location2] = ' '
                for i in range(len(self.org_plant)):
                    if self.org_plant[i].location0 == x_plant and self.org_plant[i].location1 == y_plant:
                        self.org_plant.pop(i)
                        return

    def victim_replicate(self, c_obj: Victim):
        if c_obj.hp <= 0:
            return

        x1 = c_obj.location0
        y1 = c_obj.location1

        if c_obj.type == 'D':
            if c_obj.food >= c_obj.food_max*0.7:
                if c_obj.age >= 2:
                    for i in range(len(self.org_deer)):
                        if self.org_deer[i].location0 == x1 and self.org_deer[i].location1 == y1:
                            if self.org_deer[i].location2 != c_obj.location2:
                                if c_obj.is_male == self.org_deer[i].is_male:
                                    return
                                replica_result = self.empty_place(x1, y1, 0)
                                if replica_result == -1:
                                    return
                                else:
                                    c_obj.food = c_obj.food - 0.5*c_obj.food_max
                                    c_child = Deer('Random')
                                    c_child.id = self.deer_number
                                    self.deer_number += 1
                                    c_child.location0 = x1
                                    c_child.location1 = y1
                                    c_child.location2 = replica_result
                                    self.meadow_table.scene[x1][y1][replica_result] = 'D'
                                    self.org_deer.append(c_child)

        if c_obj.type == 'S':
            if c_obj.food >= c_obj.food_max * 0.7:
                if c_obj.age >= 1:
                    for i in range(len(self.org_squirrel)):
                        if self.org_squirrel[i].location0 == x1 and self.org_squirrel[i].location1 == y1:
                            if self.org_squirrel[i].location2 != c_obj.location2:
                                if c_obj.is_male == self.org_squirrel[i].is_male:
                                    return
                                replica_result = self.empty_place(x1, y1, 0)
                                if replica_result == -1:
                                    return
                                else:
                                    c_obj.food = c_obj.food - 0.4 * c_obj.food_max
                                    c_child = Squirrel('Random')
                                    c_child.id = self.squirrel_number
                                    self.squirrel_number += 1
                                    c_child.location0 = x1
                                    c_child.location1 = y1
                                    c_child.location2 = replica_result
                                    self.meadow_table.scene[x1][y1][replica_result] = 'S'
                                    self.org_squirrel.append(c_child)

        if c_obj.type == 'R':
            if c_obj.food >= c_obj.food_max * 0.7:
                if c_obj.age >= 0:
                    for i in range(len(self.org_rabbit)):
                        if self.org_rabbit[i].location0 == x1 and self.org_rabbit[i].location1 == y1:
                            if self.org_rabbit[i].location2 != c_obj.location2:
                                if c_obj.is_male == self.org_rabbit[i].is_male:
                                    return
                                replica_result = self.empty_place(x1, y1, 0)
                                if replica_result == -1:
                                    return
                                else:
                                    c_obj.food = c_obj.food - 0.4 * c_obj.food_max
                                    c_child = Rabbit('Random')
                                    c_child.id = self.rabbit_number
                                    self.rabbit_number += 1
                                    c_child.location0 = x1
                                    c_child.location1 = y1
                                    c_child.location2 = replica_result
                                    self.meadow_table.scene[x1][y1][replica_result] = 'R'
                                    self.org_rabbit.append(c_child)

    def victim_age(self, c_obj: Victim, order: int):
        c_obj.age = c_obj.age + 1
        c_obj.hp = c_obj.hp - 1
        c_obj.food = c_obj.food - 3

        if c_obj.food <= 0.1 * c_obj.food_max:
            c_obj.hp = c_obj.hp - 3

        if c_obj.hp <= 0 or c_obj.age >= c_obj.age_max:
            self.meadow_table.scene[c_obj.location0][c_obj.location1][c_obj.location2] = ' '

            if c_obj.type == 'R':
                self.org_rabbit.pop(order)
            if c_obj.type == 'S':
                self.org_squirrel.pop(order)
            if c_obj.type == 'D':
                self.org_deer.pop(order)

    def predator_move(self, c_obj: Predator):
        x = c_obj.location0
        y = c_obj.location1
        direction = random.randint(1,4)
        variations = 0
        current_width = self.meadow_table.width
        current_height = self.meadow_table.height

        if c_obj.food <= 0.7 * c_obj.food_max:
            deer_obj = self.return_deer(x, y)
            rabbit_obj = self.return_rabbit(x, y)
            squirrel_obj = self.return_squirrel(x, y)

            if deer_obj.location0 == x and deer_obj.location1 == y:
                return
            if rabbit_obj.location0 == x and rabbit_obj.location1 == y:
                return
            if squirrel_obj.location0 == x and squirrel_obj.location1 == y:
                return

        while variations < current_width * current_height:
            if direction == 1:
                index = self.empty_place(x, y-1, 0)
                if index != -1:
                    c_obj.location1 = y-1
                    c_obj.location2 = index
                    break
                else:
                    direction = random.randint(1,4)

            if direction == 2:
                index = self.empty_place(x, y + 1, 0)
                if index != -1:
                    c_obj.location1 = y + 1
                    c_obj.location2 = index
                    break
                else:
                    direction = random.randint(1, 4)

            if direction == 3:
                index = self.empty_place(x + 1, y, 0)
                if index != -1:
                    c_obj.location0 = x + 1
                    c_obj.location2 = index
                    break
                else:
                    direction = random.randint(1, 4)

            if direction == 4:
                index = self.empty_place(x - 1, y, 0)
                if index != -1:
                    c_obj.location0 = x - 1
                    c_obj.location2 = index
                    break
                else:
                    direction = random.randint(1, 4)

            variations += 1

        self.meadow_table.scene[c_obj.location0][c_obj.location1][c_obj.location2] = c_obj.type

    def predator_eat(self, c_obj: Predator):
        x = c_obj.location0
        y = c_obj.location1

        if c_obj.food <= 0.7 * c_obj.food_max:
            deer_obj = self.return_deer(x, y)
            rabbit_obj = self.return_rabbit(x, y)
            squirrel_obj = self.return_squirrel(x, y)
            x_deer = deer_obj.location0
            y_deer = deer_obj.location1
            x_rabbit = rabbit_obj.location0
            y_rabbit = rabbit_obj.location1
            x_squirrel = squirrel_obj.location0
            y_squirrel = squirrel_obj.location1

            if x_deer == x and y_deer == y:
                if c_obj.damage >= deer_obj.hp:
                    if c_obj.food + 20 >= c_obj.food_max:
                        c_obj.food = c_obj.food_max
                    else:
                        c_obj.food = c_obj.food + 20
                    self.meadow_table.scene[x_deer][y_deer][deer_obj.location2] = ' '
                    for i in range(len(self.org_deer)):
                        if self.org_deer[i].location0 == x_deer and self.org_deer[i].location1 == y_deer:
                            self.org_deer.pop(i)
                            return
                else:
                    if c_obj.food + 10 >= c_obj.food_max:
                        c_obj.food = c_obj.food_max
                    else:
                        c_obj.food = c_obj.food + 10
                    for i in range(len(self.org_deer)):
                        if self.org_deer[i].location0 == x_deer and self.org_deer[i].location1 == y_deer:
                            self.org_deer[i].hp = self.org_deer[i].hp - c_obj.damage
                            return

            if x_rabbit == x and y_rabbit == y:
                if c_obj.damage >= rabbit_obj.hp:
                    if c_obj.food + 10 >= c_obj.food_max:
                        c_obj.food = c_obj.food_max
                    else:
                        c_obj.food = c_obj.food + 10
                    self.meadow_table.scene[x_rabbit][y_rabbit][rabbit_obj.location2] = ' '
                    for i in range(len(self.org_rabbit)):
                        if self.org_rabbit[i].location0 == x_rabbit and self.org_rabbit[i].location1 == y_rabbit:
                            self.org_rabbit.pop(i)
                            return
                else:
                    if c_obj.food + 4 >= c_obj.food_max:
                        c_obj.food = c_obj.food_max
                    else:
                        c_obj.food = c_obj.food + 4
                    for i in range(len(self.org_rabbit)):
                        if self.org_rabbit[i].location0 == x_rabbit and self.org_rabbit[i].location1 == y_rabbit:
                            self.org_rabbit[i].h = self.org_rabbit[i].hp - c_obj.damage
                            return

            if x_squirrel == x and y_squirrel == y:
                if c_obj.damage >= squirrel_obj.hp:
                    if c_obj.food + 8 >= c_obj.food_max:
                        c_obj.food = c_obj.food_max
                    else:
                        c_obj.food = c_obj.food + 8
                    self.meadow_table.scene[x_squirrel][y_squirrel][squirrel_obj.location2] = ' '
                    for i in range(len(self.org_squirrel)):
                        if self.org_squirrel[i].location0 == x_squirrel and self.org_squirrel[i].location1 == y_squirrel:
                            self.org_squirrel.pop(i)
                            return
                else:
                    if c_obj.food + 2 >= c_obj.food_max:
                        c_obj.food = c_obj.food_max
                    else:
                        c_obj.food = c_obj.food + 2
                    for i in range(len(self.org_squirrel)):
                        if self.org_squirrel[i].location0 == x_squirrel and self.org_squirrel[i].location1 == y_squirrel:
                            self.org_squirrel[i].hp = self.org_squirrel[i].hp - c_obj.damage
                            return

    def predator_replicate(self, c_obj: Predator):
        if c_obj.hp <= 0:
            return

        x1 = c_obj.location0
        y1 = c_obj.location1

        if c_obj.type == 'B':
            if c_obj.food >= c_obj.food_max * 0.7:
                if c_obj.age >= 2:
                    for i in range(len(self.org_bear)):
                        if self.org_bear[i].location0 == x1 and self.org_bear[i].location1 == y1:
                            if self.org_bear[i].location2 != c_obj.location2:
                                if c_obj.is_male == self.org_bear[i].is_male:
                                    return
                                replica_result = self.empty_place(x1, y1, 0)
                                if replica_result == -1:
                                    return
                                else:
                                    c_obj.food = c_obj.food - 0.5 * c_obj.food_max
                                    c_child = Bear('Random')
                                    c_child.id = self.bear_number
                                    self.bear_number += 1
                                    c_child.location0 = x1
                                    c_child.location1 = y1
                                    c_child.location2 = replica_result
                                    self.meadow_table.scene[x1][y1][replica_result] = 'B'
                                    self.org_bear.append(c_child)

        if c_obj.type == 'W':
            if c_obj.food >= c_obj.food_max * 0.7:
                if c_obj.age >= 2:
                    for i in range(len(self.org_wolf)):
                        if self.org_wolf[i].location0 == x1 and self.org_wolf[i].location1 == y1:
                            if self.org_wolf[i].location2 != c_obj.location2:
                                if c_obj.is_male == self.org_wolf[i].is_male:
                                    return
                                replica_result = self.empty_place(x1, y1, 0)
                                if replica_result == -1:
                                    return
                                else:
                                    c_obj.food = c_obj.food - 0.5 * c_obj.food_max
                                    c_child = Wolf('Random')
                                    c_child.id = self.wolf_number
                                    self.wolf_number += 1
                                    c_child.location0 = x1
                                    c_child.location1 = y1
                                    c_child.location2 = replica_result
                                    self.meadow_table.scene[x1][y1][replica_result] = 'W'
                                    self.org_wolf.append(c_child)

    def predator_age(self, c_obj: Predator, order: int):
        c_obj.age = c_obj.age + 1
        c_obj.hp = c_obj.hp - 5
        c_obj.food = c_obj.food - 3

        if c_obj.food <= 0.1 * c_obj.food_max:
            c_obj.hp = c_obj.hp - 10

        if c_obj.hp <= 0 or c_obj.age >= c_obj.age_max:
            self.meadow_table.scene[c_obj.location0][c_obj.location1][c_obj.location2] = ' '

            if c_obj.type == 'B':
                self.org_bear.pop(order)
            if c_obj.type == 'W':
                self.org_wolf.pop(order)

    def tick(self):
        plant_count = len(self.org_plant)
        rabbit_count = len(self.org_rabbit)
        deer_count = len(self.org_deer)
        squirrel_count = len(self.org_squirrel)
        bear_count = len(self.org_bear)
        wolf_count = len(self.org_wolf)

        #plant moves
        for i in range(plant_count):
            self.plant_replicate(self.org_plant[i])
        for i in reversed(range(plant_count)):
            self.plant_age(self.org_plant[i], i)

        #deer moves
        for i in range(deer_count):
            for j in range(self.org_deer[i].moves):
                self.victim_move(self.org_deer[i])
        for i in range(deer_count):
            self.victim_eat(self.org_deer[i])
        for i in range(deer_count):
            self.victim_replicate(self.org_deer[i])
        for i in reversed(range(deer_count)):
            self.victim_age(self.org_deer[i], i)

        #rabbit moves
        for i in range(rabbit_count):
            for j in range(self.org_rabbit[i].moves):
                self.victim_move(self.org_rabbit[i])
        for i in range(rabbit_count):
            self.victim_eat(self.org_rabbit[i])
        for i in range(rabbit_count):
            self.victim_replicate(self.org_rabbit[i])
        for i in reversed(range(rabbit_count)):
            self.victim_age(self.org_rabbit[i], i)

        #squirrel moves
        for i in range(squirrel_count):
            for j in range(self.org_squirrel[i].moves):
                self.victim_move(self.org_squirrel[i])
        for i in range(squirrel_count):
            self.victim_eat(self.org_squirrel[i])
        for i in range(squirrel_count):
            self.victim_replicate(self.org_squirrel[i])
        for i in reversed(range(squirrel_count)):
            self.victim_age(self.org_squirrel[i], i)

        #wolf moves
        for i in range(wolf_count):
            for j in range(self.org_wolf[i].moves):
                self.predator_move(self.org_wolf[i])
        for i in range(wolf_count):
            self.predator_eat(self.org_wolf[i])
        for i in range(wolf_count):
            self.predator_replicate(self.org_wolf[i])
        for i in reversed(range(wolf_count)):
            self.predator_age(self.org_wolf[i], i)

        #bear moves
        for i in range(bear_count):
            for j in range(self.org_bear[i].moves):
                self.predator_move(self.org_bear[i])
        for i in range(bear_count):
            self.predator_eat(self.org_bear[i])
        for i in range(bear_count):
            self.predator_replicate(self.org_bear[i])
        for i in reversed(range(bear_count)):
            self.predator_age(self.org_bear[i], i)
        self.update_map()
        self.show()
