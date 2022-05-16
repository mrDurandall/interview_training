# Задание 4

# Написать программу «Банковский депозит».
# Клиент банка делает депозит на определенный срок.
#
# В зависимости от суммы и срока вклада определяется процентная ставка:
# 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых).
# 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых).
# 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых).
#
# Проценты начисляются на депозит в конце каждого месяца.
#
# Необходимо написать функцию, в которую будут передаваться параметры:
# сумма вклада и срок вклада (в месяцах), а на выходе возвращать сумму вклада на конец срока.


def deposit(initial_money, number_of_months):

    terms = {
        (1000, 10000): (0.05, 0.06, 0.05),
        (10000, 100000): (0.06, 0.07, 0.065),
        (100000, 1000000): (0.07, 0.08, 0.075),
    }

    if initial_money < list(terms.keys())[0][0] or initial_money > list(terms.keys())[-1][-1]:
        raise ValueError('Неверная сумма!')
    if number_of_months % 12 != 0 and number_of_months != 6 or number_of_months < 1:
        raise ValueError('Неверный срок вклада!')

    current_money = initial_money

    # Условно принимаем, что значения суммы и срока могут быть только коректными
    # сумма в пределах от 1000 до 1000000, срок 6, 12 и более месяцев
    for total, percents in terms.items():
        if total[0] <= initial_money < total [1]:
            if number_of_months == 6:
                percent = percents[0]
            elif number_of_months == 12:
                percent = percents[1]
            elif number_of_months >= 24:
                percent = percents[2]
            break

    for month in range(number_of_months):
        current_money += current_money * (percent / 12)
        current_money = round(current_money, 2)

    return current_money


def main():

    total_deposit = int(input('Введите сумму вклада: '))
    number_of_month = int(input('Введите срок вклада: '))
    print(deposit(total_deposit, number_of_month))


if __name__ == '__main__':
    main()
