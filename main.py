from online import get_currencies


# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 7. Вывод результата

online_response = get_currencies()


def convert(amount, from_ticker, to_ticker, currencies):
    from_currency = currencies.get(from_ticker)
    to_currency = currencies.get(to_ticker)

    coefficient = to_currency / from_currency
    return round(amount * coefficient, 2)


def input_currency(input_message, currencies, prev_ticker=None):
    while True:
        ticker = input(f"{input_message}: ").strip()
        selected_currency = currencies.get(ticker, None)

        if selected_currency is None:
            print(f'Валюты {ticker} не существует, выберите валюту из представленных выше')
        elif prev_ticker is not None and prev_ticker == ticker:
            print(f'Выберите валюту отличную от исходной')
        else:
            return ticker


print("Привет, это программа Конвертер Валют!")

print("""
Для работы с программой требуется:
- выбрать исходную валюту 
- выбрать в какую валюту следует перевести
- ввести количество исходной валюты

Доступные валюты:
""")

for currency in online_response['data']:
    print(f'- {currency}')


from_ticker = input_currency("Введите исходную валюту", online_response['data'])
to_ticker = input_currency("Введите в какую валюту следует перевести", online_response['data'], from_ticker)

amount_input = input("Введите количество валюты: ")
amount = float(amount_input)

result = convert(amount, from_ticker, to_ticker, online_response['data'])

print(f'Результат: {amount} {from_ticker} = {result} {to_ticker}')
