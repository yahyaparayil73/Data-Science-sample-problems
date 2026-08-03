def print_shopping_items(*items):
    # 'items' inside the function is a TUPLE containing all passed positional arguments
    print(f"Type of items: {type(items)}")
    print("Items to buy:")
    for item in items:
        print(f"- {item}")

# You can pass 2, 4, or zero arguments!
print_shopping_items()
print("-" * 20)
print_shopping_items("Apples", "Rice", "Eggs", "Coffee")