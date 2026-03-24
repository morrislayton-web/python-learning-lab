# Inventory Dictionary
inventory = {
    "Cement": 50,
    "Plywood": 20,
    "Nails": 100
}

item_to_check = "Cement"
if item_to_check in inventory:
    print(f"We have {inventory[item_to_check]} bags of {item_to_check} left.")
else:
    print("Item not found in warehouse.")
