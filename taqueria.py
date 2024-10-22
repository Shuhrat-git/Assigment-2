# Menu with items and their prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_cost = 0.0                            # Initialize total cost to 0

    while True:
        try:
            item = input("Item: ").title()      # Add input and convert to title case
            if item in menu:
                total_cost += menu[item]        # Add the price of the item to the total cost
                print(f"${total_cost:.2f}")     # Display the running total formatted to 2 decimal places
            else:
                print("Not found item in menu") # If item is not in the menu, ignore it
                continue

        except EOFError:                        # Catch EOFError (Linux/macOS) control-d or (Windows) control-z
                print()                         # Print a newline to keep the prompt clean
                break

if __name__ == "__main__":
    main()
