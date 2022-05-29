# 5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в
# функцию должна передаваться фиксированная ежемесячная сумма пополнения
# вклада. Считаем, что клиент вносит средства в последний день каждого


def deposit(initial_money, number_of_months, monthly_payment):

    current_money = initial_money

    terms = {
        (1000, 10000): (0.05, 0.06, 0.05),
        (10000, 100000): (0.06, 0.07, 0.065),
        (100000, 1000000): (0.07, 0.08, 0.075),
    }

    if initial_money < list(terms.keys())[0][0] or initial_money > list(terms.keys())[-1][-1]:
        raise ValueError('Неверная сумма!')
    if number_of_months % 12 != 0 and number_of_months != 6 or number_of_months < 1:
        raise ValueError('Неверный срок вклада!')
    if monthly_payment < 1:
        raise ValueError('Неверная сумма ежемесячного платежа!')

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
        if month and month != number_of_months - 1:
            current_money += monthly_payment
        print(current_money)

    return current_money


def main():
    print(deposit(2000, 12, 100))


if __name__ == '__main__':
    main()