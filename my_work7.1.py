from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category


    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    _file_name = 'products.txt'


    def get_products(self):
        file = open('products.txt', 'r')
        list = file.read()
        pprint(file.read())
        file.close()
        return list


    def add(self, *products):
        s1.get_products()
        i = 0
        for i in products:
            print(type(i))
            if products[i][0] in list:
                print(f'Продукт {products[i][0]} уже есть в магазине')
            else:
                file = open('products.txt', 'a')
                file.write('products[i]')
                file.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p3)
s1.get_products()
#s1.add(p1, p2, p3)

print(s1.get_products())