num = int(input("give me a number to check: "))
check = int(input("give me a number to divided by: "))

if num % 4 == 0:
    print(num, "is multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
# tuple
stock_prices = [("APPL", 200), ("GOOG", 400), ("MSFT", 100)]
for item in stock_prices:
    print(item)
