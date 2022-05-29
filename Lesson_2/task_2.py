# Задание 2

# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
# Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.


class ItemDiscount:

    __name = 'Apple'
    __price = 300

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_item_data(self):
        print(f'{self.get_name()} - {self.get_price()}')


def main():

    apple = ItemDiscount()
    apple_report = ItemDiscountReport()
    apple_report.get_item_data()


if __name__ == '__main__':
    main()
