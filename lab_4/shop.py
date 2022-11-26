class shop():

    def __init__(self):
        self.__list_of_product = []
        self.__id = 0
        self.__name = 0

    def create_product(self, name, count, price):
        if self.__check_count(count):
            new_product = product(name, count, price, self.__id)
            self.__id += 1
            self.__list_of_product.append(new_product)
        else:
            print('ERROR: product not been created - bad arguments')

    def __check_count(self, count):
        if count >= 0:
            return True
        else:
            return False

    def delete_product(self, id):
        prod = self.search_product_by_id(id)
        # index = self.__list_of_product.index(prod)
        # self.__list_of_product.pop(index)
        self.__list_of_product.remove(prod)

    def buy_product(self, name, count):
        for prod in self.__list_of_product:
            if prod.get_name() == name and prod.get_count() >= count:
                prod.set_count_product(count)
            return prod
            #     print("Продукт успешно куплен")
            #     self.__list_of_product.remove(prod)
            #     return prod
            # else:
            #     print("Продукта нет на складе")
            #     return prod

    def search_product_by_id(self, id):
        for prod in self.__list_of_product:
            if prod.get_id() == id:
                print("product - find")
            else:
                print("Неверные данные")
                return prod

    def search_product_by_name(self, name):
        for prod in self.__list_of_product:
            if prod.get_name() == name:
                print("product_name - find")
                return prod

    def search_product_by_price(self, x_price, y_price):
        temp = []
        for prod in self.__list_of_product:
            p = prod.get_price()
            if x_price <= prod.get_price() and y_price >= prod.get_price():
                temp.append(prod.get_product())
                # print(f"Минимиальная цена: {min(temp)}", f"Максимальная цена: {max(temp)}")
        return temp

    def modification_product_name(self, id, new_name):
        prod = self.search_product_by_id(id)
        prod.set_name_product(new_name)

    def modification_product_count(self, id, new_count):
        prod = self.search_product_by_id(id)
        prod.set_count_product(new_count)

    def modification_product_price(self, id, new_price):
        prod = self.search_product_by_id(id)
        prod.set_price_product(new_price)

    def modification_product_feature(self, id, name_feature, new_value):
        prod = self.search_product_by_id(id)
        prod.set_feature(name_feature, new_value)

    def get_list_of_product(self):
        return self.__list_of_product

    def show_all_products(self):
        for prod in self.__list_of_product:
            print(prod.get_product())


class product():

    def __init__(self, name, count, price, id):
        self.__name = name
        self.__count = count
        self.__price = price
        self.__id = id
        self.__feature = {}

        # self.set_feature('color', '#cecece')
        # self.set_feature('size', '60')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_count(self):
        return self.__count

    def get_price(self):
        return self.__price

    def get_product(self):
        result = (self.__id, self.__name, self.__count, self.__price,
                  self.__feature)
        return result

    def set_feature(self, feature, value):
        self.__feature[feature] = value

    def set_name_product(self, new_name):
        self.__name = new_name

    def set_count_product(self, new_count):
        self.__count = new_count

    def set_price_product(self, new_price):
        self.__price = new_price

    def x_price(self, x_price):
        self.__price = x_price

    def y_price(self, y_price):
        self.__price = y_price


# Ядро
my_s = shop()

# Создание товара формата: имя, количество, цена
my_s.create_product('first', 10, 50)
my_s.create_product('second', 30, 66)
my_s.create_product('therd', 1, 5000)
my_s.create_product('tovar1', 1, 55)
my_s.create_product('tovar2', 3, 34)
my_s.create_product('tovar3', 8, 44)
my_s.create_product('tovar4', 4, 65)
my_s.create_product('tovar5', 2, 100)
my_s.create_product('tovar6', 1, 12)
my_s.create_product('tovar7', 10, 999)
my_s.create_product('tovar8', 5, 6000)
my_s.create_product('tovar10', 100, 15)
my_s.create_product('tovar9', 90, 4500)
# my_s.show_all_products()

# Честно не хочу знать что это за чудище
# my_s.modification_product_name(1, "NEW NAME")
# my_s.modification_product_count(1, 0)
# my_s.modification_product_price(1, "ФИГАЛЛИОН")
# my_s.show_all_products()
# my_s.delete_product(1)
# my_s.show_all_products()

# Поиск по имени / айди / в диапазоне
# my_s.search_product_by_name('therd')
# my_s.search_product_by_id("l")
# my_s.search_product_by_price("lambda")
# print(my_s.search_product_by_price(50, 60))
# my_s.show_all_products()

# Покупка товара
# my_s.buy_product("first", 10)
my_s.show_all_products()
my_s.buy_product("first", 5)
print("TEST")
my_s.show_all_products()
