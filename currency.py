currencies = ["EUR", "GBP", "CNY", "INR"]
rates = [1.08, 1.21, 0.15, 0.012]

choice = int(input("Choose to convert to 1. EUR 2. GBP 3. CNY 4. INR: "))

dollar_input = input("Enter dollar amount to exchange: ")

dollars = float(dollar_input[1:])

after_fee = dollars * 0.95

currency = currencies[choice - 1]
rate = rates[choice - 1]

converted_amount = after_fee / rate

converted_amount = round(converted_amount)

print("After fees you will receive", currency, converted_amount)