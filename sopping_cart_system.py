products = []


while True:
    choice = int(
        input(
            "1 : Add \n2 : Remove \n3: List All Items \n4: Total Cost \npress any key to exit"
        )
    )

    if choice == 1:
        name = input("Enter proudct name: ")
        price = float(input("Enter proudct price: "))
        quantity = int(input("Enter quantity: "))

        item = {"name": name, "price": price, "quantity": quantity}

        products.append(item)

        print("Product Added !!!!!")

    elif choice == 2:

        user_choise_name = input("Enter the name of product you want to delete: ")
        is_product_found = False

        for item in products:
            if user_choise_name == item["name"]:
                products.remove(item)
                is_product_found = True

        if is_product_found:
            print("Product Deleted !!!")
        else:
            print("Product Not Found!!!")

    elif choice == 3:
        # Display all items
        print("\n")
        print("*" * 100)
        for item in products:
            print(
                f"Name:{item['name']} Quantity: {item['quantity']} Price: {item['price']} Total:{item['price'] * item['quantity'] } "
            )

        print("*" * 100)
        print("\n")
    elif choice == 4:
        total_price = 0.0
        for item in products:
            item_total_price = item["price"] * item["quantity"]
            total_price = total_price + item_total_price

        print(f"Your Total Price is : {total_price}")
    else:
        print("Thank YOU")
        break
