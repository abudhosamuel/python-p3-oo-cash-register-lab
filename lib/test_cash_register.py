from cash_register import CashRegister

# Create a CashRegister instance without a discount
register = CashRegister()

# Add items to the register
register.add_item("apple", 0.99)
print(f"Total after adding apple: {register.total}")

register.add_item("tomato", 1.76, 2)  # Adding 2 tomatoes
print(f"Total after adding 2 tomatoes: {register.total}")

# Apply a discount (since this register has no discount, expect a specific message)
register.apply_discount()

# Void the last transaction
register.void_last_transaction()
print(f"Total after voiding last transaction: {register.total}")

# Create another CashRegister instance with a 20% discount
register_with_discount = CashRegister(20)

# Add an expensive item
register_with_discount.add_item("macbook air", 1000)
print(f"Total after adding macbook air: {register_with_discount.total}")

# Apply the discount
register_with_discount.apply_discount()
print(f"Total after applying discount: {register_with_discount.total}")

# Add more items to check the items list
register_with_discount.add_item("notebook", 5.00, 3)  # Adding 3 notebooks
print(f"Items in the register: {register_with_discount.items}")
