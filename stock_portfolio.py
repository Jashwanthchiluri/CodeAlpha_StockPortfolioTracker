# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Get stock details from the user
while True:
    stock = input(
        "\nEnter stock name (or type 'done' to finish): "
    ).strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock name. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    # Store the stock quantity
    portfolio[stock] = portfolio.get(stock, 0) + quantity

    print(f"Added {quantity} shares of {stock}.")

# Calculate the total investment
total_investment = 0

print("\n================================")
print("       PORTFOLIO SUMMARY")
print("================================")

if not portfolio:
    print("No stocks were added.")

else:
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        print(
            f"{stock}: {quantity} shares x "
            f"${price} = ${investment}"
        )

    print("--------------------------------")
    print(f"Total Investment: ${total_investment}")

# Save the portfolio to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=======================\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock}: {quantity} shares, "
            f"Investment: ${investment}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}\n")

print("\nPortfolio saved to portfolio_summary.txt")
print("Thank you for using Stock Portfolio Tracker!")