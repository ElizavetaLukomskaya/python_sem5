import random

# Constructor class about organism
class Organism(object):
    def __init__(self, type, age, age_max, id, hp, hp_max, food, food_max, moves, is_male):
        self._type = type
        self._age = age
        self._age_max = age_max
        self._id = id
        self._hp = hp
        self._hp_max = hp_max
        self._food = food
        self._food_max = food_max
        self._moves = moves
        self._is_male = is_male
        _location = [0, 0, 0]

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def age_max(self):
        return self._age_max

    @age_max.setter
    def age_max(self, age_max):
        self._age_max = age_max

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def hp_max(self):
        return self._hp_max

    @hp_max.setter
    def hp_max(self, hp_max):
        self._hp_max = hp_max

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, food):
        self._food = food

    @property
    def food_max(self):
        return self._food_max

    @food_max.setter
    def food_max(self, food_max):
        self._food_max = food_max

    @property
    def moves(self):
        return self._moves

    @moves.setter
    def moves(self, moves):
        self._moves = moves

    @property
    def is_male(self):
        return self._is_male

    @property
    def location0(self):
        return self._location[0]

    @location0.setter
    def location0(self, count):
        self._location[0] = count

    @property
    def location1(self):
        return self._location[1]

    @location1.setter
    def location1(self, count):
        self._location[1] = count

    @property
    def location2(self):
        return self._location[2]

    @location2.setter
    def location2(self, count):
        self._location[2] = count


class Predator(Organism):
    def __init__(self):
        self._damage = 0

    @property
    def damage(self):
        return self._damage


class Victim(Organism):
    def __init__(self):
        pass


class Plant(Organism):
    def __init__(self):
        self._hp_max = 2
        self._hp = self._hp_max
        self._moves = 0
        self._age = 0
        self._age_max = 0
        self._type = 'P'
        self._location = [0, 0, 0]


class Bear(Predator):
    def __init__(self, sex):
        sex_list = [True, False]
        self._hp_max = 500
        self._hp = self._hp_max
        self._food_max = 150
        self._food = self._food_max
        self._moves = 3
        self._damage = 100
        self._age = 0
        self._age_max = 30
        self._type = 'B'
        self._location = [0, 0, 0]
        if sex == 'Male':
            self._is_male = True
        if sex == 'Female':
            self._is_male = False
        if sex == 'Random':
            self._is_male = random.choice(sex_list)


class Wolf(Predator):
    def __init__(self, sex):
        sex_list = [True, False]
        self._hp_max = 300
        self._hp = self._hp_max
        self._food_max = 75
        self._food = self._food_max
        self._moves = 4
        self._damage = 70
        self._age = 0
        self._age_max = 18
        self._type = 'W'
        self._location = [0, 0, 0]
        if sex == 'Male':
            self._is_male = True
        if sex == 'Female':
            self._is_male = False
        if sex == 'Random':
            self._is_male = random.choice(sex_list)


class Rabbit(Victim):
    def __init__(self, sex):
        sex_list = [True, False]
        self._hp_max = 200
        self._hp = self._hp_max
        self._food_max = 60
        self._food = self._food_max
        self._moves = 3
        self._age = 0
        self._age_max = 15
        self._type = 'R'
        self._location = [0, 0, 0]
        if sex == 'Male':
            self._is_male = True
        if sex == 'Female':
            self._is_male = False
        if sex == 'Random':
            self._is_male = random.choice(sex_list)


class Deer(Victim):
    def __init__(self, sex):
        sex_list = [True, False]
        self._hp_max = 300
        self._hp = self._hp_max
        self._food_max = 50
        self._food = self._food_max
        self._moves = 4
        self._age = 0
        self._age_max = 18
        self._type = 'D'
        self._location = [0, 0, 0]
        if sex == 'Male':
            self._is_male = True
        if sex == 'Female':
            self._is_male = False
        if sex == 'Random':
            self._is_male = random.choice(sex_list)


class Squirrel(Victim):

    def __init__(self, sex):
        sex_list = [True, False]
        self._hp_max = 150
        self._hp = self._hp_max
        self._food_max = 40
        self._food = self._food_max
        self._moves = 3
        self._age = 0
        self._age_max = 12
        self._type = 'S'
        self._location = [0, 0, 0]
        if sex == 'Male':
            self._is_male = True
        if sex == 'Female':
            self._is_male = False
        if sex == 'Random':
            self._is_male = random.choice(sex_list)
