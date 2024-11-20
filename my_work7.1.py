class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category


    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    def __init__(self):
        __file_name = 'products.txt'


    def get_products(self):
        file = open('products.txt', 'r')
        list_1 = file.read()
        file.close()
        return list_1


    def add(self, *products):
        list_1 = s1.get_products()
        i = 0
        for i in range(len(products)):
            if products[i].name in list_1:
                print(f'Продукт {products[i].name + ', ' + str(products[i].weight) + ', ' + products[i].category} уже есть в магазине')
            else:
                file = open('products.txt', 'a')
                str_1 = f'{products[i].name + ', ' + str(products[i].weight) + ', ' + products[i].category}\n'
                file.write(str_1)
                file.close()


    def clear(self):
        with open('products.txt', 'w'):
            pass


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')

print(p1.__str__())
#s1.add(p3)
#print(s1.get_products())
s1.add(p1, p2, p3)
print(s1.get_products())
#s1.clear()
#s1.get_products()
