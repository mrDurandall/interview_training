# Задание 3

# Реализовать возможность переустановки значения цены товара в родительском классе.
# Проверить, распечатать информацию о товаре.


class ItemDiscount:

    __name = 'Apple'
    __price = 300

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


class ItemDiscountReport(ItemDiscount):

    def get_item_data(self):
        print(f'{self.get_name()} - {self.get_price()}')


def main():

    apple = ItemDiscountReport()
    apple.get_item_data()
    apple.set_price(500)
    apple.get_item_data()


if __name__ == '__main__':
    main()
