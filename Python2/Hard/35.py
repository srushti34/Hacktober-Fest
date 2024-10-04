def update_inventory(inventory, item, quantity):
    try:
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
    except TypeError as e:
        print(f"TypeError: {e}")

def main():
    inventory = {"apple": 10, "banana": 5}
    update_inventory(inventory, "orange", 3)
    print(f"Updated Inventory: {inventory}")
    
    update_inventory(inventory, "banana", "five")  
    print(f"Updated Inventory: {inventory}")

main()
