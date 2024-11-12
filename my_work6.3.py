import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0


    def __init__(self, _cords, speed):
        self._cords = [0, 0, 0]
        self.speed = speed


    def move(self, dx, dy, dz):
        dx_1 = dx * self.speed
        dy_1 = dy * self.speed
        dz_1 = dz * self.speed
        if dz < 0:
            print("It's too deep, i can't dive :(")
            dz_1 = dz
        self._cords = [dx_1, dy_1, dz_1]
        return self._cords


    def get_cords(self, _cords):
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')


    def attack(self, _DEGREE_OF_DANGER):
        if _DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


    def speak(self, sound):
        print(sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        number = str(random.randint(1, 4))
        print('Here are(is) ' + number + ' eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        z = self._cords[2]
        dz = abs(dz)
        self._cords[2] = z - dz/2*self.speed
        return self._cords[2]


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
        sound = "Click-click-click"


db = Duckbill([1, 1, 1],3)

print(db.live)
print(db.beak)

db.speak(db.sound)
db.attack(5)

db.move(1, 2, 3)
db.get_cords(db._cords)

db.dive_in(6)
db.get_cords(db._cords)

db.lay_eggs()