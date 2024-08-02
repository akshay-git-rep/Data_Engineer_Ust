items = [
    {"item_id":1,"item_name":"bread","item_price":40},
    {"item_id":2,"item_name":"banana","item_price":10},
    {"item_id":3,"item_name":"milk","item_price":20},
    {"item_id":4,"item_name":"apple","item_price":30},
    {"item_id":5,"item_name":"mango","item_price":50},
    {"item_id":6,"item_name":"watermelon","item_price":80}
    ]

cart = []

def view_store():
    print("Store Items List")
    for item in items:
        print(f"ID:{item["item_id"]}, Name:{item["item_name"]}, Price:{item["item_price"]}")

def purchase_item():
    while True:
        item_name = input("Enter the name you want to purchase:")
        quantity = int(input("Enter the quantity:"))

        for item in items:
            if item_name == item["item_name"]:
                cart.append({"item_id":item["item_id"],"item_name": item_name, "item_price": item["item_price"], "quantity":quantity})
                break
        cont = input("Do you want to continue yes/no:")
        if cont.lower() != "yes":
            break

def update_purchase_item():
    item_name = input("Enter the name you want to update:")
    for item in cart:
        if item["item_name"] == item_name:
            quantity = int(input("Enter the quantity:"))
            item["quantity"] = quantity
            break

def remove_item():
    item_name = input("Enter the item you want to remove:")
    global cart
    cart = [item for item in cart if item["item_name"] != item_name]

def view_purchase():
    print("Selected items:")
    total_price=0
    for item in cart:
        total_price = item["item_price"] * item["quantity"]
        print(f"item_id: {item["item_id"]}, item_name:{item["item_name"]}, item_price:{item["item_price"]}, quantity:{item["quantity"]},Total: {total_price}")

def generate_invoice():
    total = 0
    with open("invoice.txt", "w") as file:
        file.write("********** INVOICE COPY ***********\n")
        for item in cart:
            total_price = item["item_price"] * item["quantity"]
            total += total_price
            file.write(f"{item["item_id"]}.{item["item_name"]} {item["quantity"]} {total_price}")
        file.write(f"\nTotal:{total}")
    print("Invoice generated")
    
def main_menu():
    while True:
        print("\nMenu")
        print("1. View Menu:")
        print("2. Purchase Item:")
        print("3. Update Purchase item:")
        print("4. Remove the purchase item from list:")
        print("5. View purchased item:")
        print("6. Generate Invoice:")
        choice = int(input("Enter the Choice you want:"))
        if choice == 1:
            view_store()
        elif choice == 2:
            purchase_item()
        elif choice == 3:
            update_purchase_item()
        elif choice == 4:
            remove_item()
        elif choice == 5:
            view_purchase()
        elif choice== 6:
            generate_invoice()                   
        else:
            print("invalid selection")


main_menu()
#generate_invoice()
