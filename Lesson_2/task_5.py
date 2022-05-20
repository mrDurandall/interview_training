# Задание 5

# Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
# Далее реализовать вызов каждой из функции get_info.


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


class ItemDiscountRepotFirst(ItemDiscountReport):

    def get_info(self):
        return self.get_price()


class ItemDiscountRepotSecond(ItemDiscountReport):

    def get_info(self):
        return self.get_name()


def get_info(getter_class):
    print(getter_class.get_info())


def main():

    get_info(ItemDiscountRepotFirst())
    get_info(ItemDiscountRepotSecond())


if __name__ == '__main__':
    main()
