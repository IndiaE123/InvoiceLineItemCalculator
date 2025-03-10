# India Eiland
# CIS261
# Invoice Line Item Calculator

def display_heading():
    print("\n==== Welcome to the Price Calculator ===\n")
    
def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            return price
        except ValueError:
            print("Invalid input! Please enter a valid float number for the price.")
            
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid input! Please input a valid integer for the quantity.")
            
def main():
    display_heading()
    
    while True:
        price = get_price()
        quantity = get_quantity()
        total = price * quantity

        print("\n===== Line Item =====")
        print(f"Price: ${price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total: ${total:.2f}\n")
        
        choice = input("Enter another line item? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nThank you for using the Price Calculator! Goodbye!")
            break

if __name__ == "__main__":
    main()