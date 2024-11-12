class Animal:
    alive = True
    fed = False


    def __init__(self, name):
        self.name = name


    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(self.name,'съел', food.name)
                self.fed = True
                self.alive = True
            else:
                print(self.name, 'не стал есть', food.name)
                self.alive = False
        else:
            print('Это есть нельзя!')
            self.fed = False


class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
        pass

class Predator(Animal):
        pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True


a1 = Predator('Волк')
a2 = Mammal('Кот')
p1 = Flower('репейник')
p2 = Fruit('манго')

print(a1.name)
print(a2.name)
print(p1.name)
print(p2.name)
print(a1.alive)
print(a1.fed)
print(a2.alive)
print(a2.fed)
print(p1.edible)
print(p2.edible)
a1.eat(p1)
print(a1.alive)
print(a1.fed)
a1.eat(p2)
print(a1.alive)
print(a1.fed)
a2.eat(p1)
print(a2.alive)
print(a2.fed)
a2.eat(p2)
print(a2.alive)
print(a2.fed)
a2.eat(a1)
print(a2.alive)
print(a2.fed)