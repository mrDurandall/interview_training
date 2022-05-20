# Задание 4

# Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
# Выполнить перегрузку методов конструктора дочернего класса (метод __init__,
# в который должна передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
# Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
# (вторая и третья строка после объявления дочернего класса).


class ItemDiscount:

    __name = 'Apple'
    __price = 300

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            raise ValueError
        self.__price = new_price


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount=0):
        if not 0 <= discount <= 100:
            raise ValueError
        self.__discount = discount

    def get_item_data(self):
        print(f'{self.get_name()} - {self.get_price()}, со скидкой - {self.get_price()*(1 - self.__discount/100)}')


def main():

    apple = ItemDiscountReport(50)
    apple.get_item_data()
    apple.set_price(500)
    apple.get_item_data()


if __name__ == '__main__':
    main()
