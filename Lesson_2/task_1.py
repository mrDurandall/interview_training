# Задание 1

# Создать два класса. Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре:
# название и цену. Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
# отвечающую за отображение информации о товаре в одной строке вида (“{название товара} {цена товара}”).
# Создать экземпляры родительского класса и дочернего. Распечатать информацию о товаре.


class ItemDiscount:

    name = 'Apple'
    price = 300


class ItemDiscountReport(ItemDiscount):

    def get_item_data(self):
        print(f'{self.name} - {self.price}')


def main():

    apple = ItemDiscount()
    apple_report = ItemDiscountReport()
    apple_report.get_item_data()


if __name__ == '__main__':
    main()
