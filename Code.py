#Chee Kai Jian
#TP074077

inventory_file = 'inventory.txt'
user_file = 'user.txt'



def log_in():
    user_data = []
    with open(user_file, 'r') as filehandler:
        for line in filehandler.readlines():
            items = line.strip().split(',')
            user_data.append(items)

    username = input("Enter your username: ").lower()
    password = input("Enter your password: ")
    user_type = input('''
               Grocery stock manager
           ----------------------------
           Admin
           Inventory checker
           Purchaser
           Exit 

           Enter your identity:
           ''').lower()
    item_found = False
    for user in user_data:
        if user[0] == username and user[1] == password and user[2] == user_type:
            item_found = True
            if user_type == 'admin':
                admin(user_type)
                return user_type
            if user_type == 'inventory checker':
                inventory_checker(user_type)
                return user_type
            if user_type == 'purchaser':
                purchaser(user_type)
                return user_type
    if not item_found:
        print("Identity doesn't match...")
        return log_in()


def add_new_user(user_type):
    while True:
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        usertype = input("Enter your Identity: ")
        user_info = [username, password, usertype]
        with open(user_file, 'a') as filehandler:
            user_insert = ','.join(user_info) + '\n'
            filehandler.write(user_insert)
        option_1 = input("Would u like to continue(Yes or No)")
        if option_1 == "yes".lower():
            return add_new_user(user_type)
        if option_1 == "no".lower():
            return user_type



def delete_user(user_type):
    userdata = []
    with open(user_file, 'r') as filehandler:
        for data in filehandler.readlines():
            userdata.append(data.strip())

    username = input("Enter the user you want to delete: ")

    userdata = [item for item in userdata if not item.startswith(username)]
    print("User deleted..")

    with open(user_file, 'w') as filehandler:
        filehandler.write('\n'.join(userdata) + '\n')

    option_1 = input("Would you like to continue?(Yes or No): ")
    if option_1 == "yes".lower():
        return delete_user(user_type)
    if option_1 == "no".lower():
        return user_type


def append_inventory_file(inventory):
    with open(inventory_file, 'a') as filehandler:
        for item in inventory:
            new_data = ','.join(item) + '\n'
            filehandler.write(new_data)


def write_inventory_file(inventory):
    with open(inventory_file, 'w') as filehandler:
        for item in inventory:
            new_data = ','.join(item) + '\n'
            filehandler.write(new_data)


def read_inventory():
    items = []
    with open(inventory_file, 'r') as filehandler:
        for line in filehandler.readlines():
            item = line.strip().split(',')
            items.append(item)
    return items


def item_insert(user_type):
    inventory = []
    code = input("Enter item code: ")
    item_name = input("Enter item name: ")
    category = input("Enter category: ")
    unit = input("Enter Unit: ")
    price = input("Enter price: ")
    quantity = input("Enter your quantity: ")
    minimum = input("The minimum amount of the item: ")
    item = [code, item_name, category, unit, str(price), str(quantity), minimum]
    inventory.append(item)
    append_inventory_file(inventory)
    input_1 = input("Do you wish to continue adding item?(Yes Or No):")
    if input_1 == 'yes'.lower():
        return item_insert(user_type)
    if input_1 == 'no'.lower():
        return user_type
    else:
        print("Please try again..")



def delete_item(user_type):
    code = input("Enter the item (code) you want to delete: ")
    items = read_inventory()
    item_found = False
    inventory = []
    for item in items:
        if code == item[0]:
            item_found = True
            print("Item has been deleted")
        else:
            inventory.append(item)
    with open(inventory_file, 'w') as filehandler:
        for item in inventory:
            new_data = ','.join(item) + '\n'
            filehandler.write(new_data)
    if item_found is True:
        option_1 = input("Do you wish to continue ?(Yes Or No):").lower()
        if option_1 == "yes":
            return delete_user(user_type)
        if option_1 == "no":
            return user_type
    if not item_found:
        print('Item not found')
        option_2 = input("Do you wish to continue ?(Yes Or No):").lower()
        if option_2 == "yes":
            return delete_user(user_type)
        if option_2 == "no":
            return user_type


def update_inventory(user_type):
    items = read_inventory()
    inventory = []
    codenotfound = True
    item_found = False
    item_number = input("Enter the item(code) you want to update: ")
    for item in items:
        if item_number == item[0]:
            item_found = True
            new_code = input("Enter new item code: ")
            new_name = input("Enter new item name: ")
            new_category = input("Enter new category: ")
            new_unit = input("Enter new unit: ")
            new_price = input("Enter new price: ")
            new_quantity = input("Enter new quantity: ")
            new_minimum = input("Enter new minimum: ")
            updated_item = [new_code, new_name, new_category, new_unit, new_price, new_quantity, new_minimum]
            inventory.append(updated_item)

            codenotfound = False
            print("Item Updated!")
        else:
            inventory.append(item)

    if not item_found:
        print("Item not found...")
    write_inventory_file(inventory)



    if item_found is True:
        option_1 = input("Do you wish to continue ?(Yes Or No):").lower()
        if option_1 == "yes":
            return update_inventory(user_type)
        if option_1 == "no":
            return user_type

    if not codenotfound:
        option_2 = input("Do you wish to continue ?(Yes Or No):").lower()
        if option_2 == "yes":
            return update_inventory(user_type)
        if option_2 == "no":
            return user_type



def stock_taking(user_type):
    code = input("Enter the item(code) you want to take: ")
    inventory = read_inventory()

    item_found = False
    for item in inventory:
        if code == item[0]:
            print("The quantity of the item is " + item[5])
            option_1 = input("Confirm or change? :")
            if option_1 == 'confirm'.lower():
                item_found = True
                option_2 = input("Do you wish to continue ?(Yes Or No):").lower()
                if option_2 == "yes":
                    return stock_taking(user_type)
                if option_2 == "no":
                    return user_type

            if option_1 == 'change'.lower():
                item_found = True
                new_quantity = input("Enter your new Quantity: ")
                item[5] = new_quantity
                print("Item's quantity changed successfully")
                option_2 = input("Do you wish to continue ?(Yes Or No):").lower()
                if option_2 == "yes":
                    return stock_taking(user_type)
                if option_2 == "no":
                    return user_type

    if not item_found:
        print("The item doesnt exist...")
        option_1 = input("Do you wish to continue ?(Yes Or No):").lower()
        if option_1 == "yes":
            return stock_taking(user_type)
        if option_1 == "no":
            return user_type

    write_inventory_file(inventory)


def view_replenish():
    inventory = read_inventory()
    item_found = False

    for i in inventory:
        quantity = int(i[5])
        minimum_stock = int(i[6])
        if minimum_stock > quantity:
            print(i)
            item_found = True
    if not item_found:
        print("All items are above the minimum quantity")


def stock_replenishment(user_type):
    inventory = read_inventory()
    code = input("Enter code of Item: ")
    item_found = False
    for item in inventory:
        if item[0] == code:
            item_found = True
            print(f"The quantity of this particular item is {item[5]}")
            option_1 = input("Do you want to update the quantity of this item?(yes or no) : ").lower()
            if option_1 == 'yes':
                new_quantity = input("New quantity: ")
                item[5] = new_quantity
                print("Quantity of the item has been updated")
                option_3 = input("Do you wish to continue?(yes or no): ").lower()
                if option_3 == 'yes':
                    return stock_replenishment(user_type)
                if option_3 == 'no':
                    return user_type

            elif option_1 == 'no':
                return user_type

    if not item_found:
        print("Item cannot be found...")
        option_2 = input("""
            1-Continue
            2-Return to menu
            """).lower()
        if option_2 == "continue" or '1':
            return stock_replenishment(user_type)
        if option_2 == "return to menu" or '2':
            return user_type
    write_inventory_file(inventory)


def search(user_type):
    while True:
        inventory = read_inventory()
        option_1 = input('''
            --------------
            1- Description
            2- Code range
            3- Category
            4- Price range
            5- Exit
            --------------
            Enter Method of item Search: ''').lower()



        if (option_1 == 'description') or (option_1 == "1"):
            description = input("Enter item description to search: ").lower()
            found_items = []
            item_found = False
            for item in inventory:
                if description.lower() == item[1].lower():
                    found_items.append(item)
                    item_found = True

            if item_found:
                print("Search Results:")
                for item in found_items:
                    i = ','.join(item) + '\n'
                    print(i)
                    option_2 = input("""
                    1-Continue
                    2-Return to menu
                    """)
                    if option_2.lower() == "continue" or option_2 == "1":
                        return search(user_type)
                    if option_2.lower() == "return to menu" or option_2 == "2":
                        return user_type

            if not item_found:
                print("Item not found...")
                option_2 = input("""
                            1-Continue
                            2-Return to menu
                            """)
                if option_2.lower() == "continue" or  option_2 == "1":
                    return search(user_type)
                if option_2.lower() == "return to menu" or option_2 == "2":
                    return user_type



        if (option_1 == 'code range') or (option_1 == "2"):
            min_code = int(input("Enter minimum code: "))
            max_code = int(input("Enter maximum code: "))
            item_found = False
            for item in inventory:
                code = int(item[0])
                if min_code <= code <= max_code:
                    item_found = True
                    print(item)

            if item_found:
                option_3 = input("""
                                1-Continue
                                2-Return to menu
                                """)
                if option_3.lower() == "continue" or option_3 == "1":
                    return search(user_type)
                if option_3.lower() == "return to menu" or option_3 == "2":
                    return user_type

            if not item_found:
                print("Item not found...")
                option_3 = input("""
                                1-Continue
                                2-Return to menu
                                """)
                if option_3.lower() == "continue" or option_3 == "1":
                    return search(user_type)
                if option_3.lower() == "return to menu" or option_3 == "2":
                    return user_type





        if (option_1 == 'category') or (option_1 == "3"):
            category = input("Enter item category to search: ")
            item_found = False
            for item in inventory:
                if category.lower() == item[2].lower():
                    item_found = True
                    print(item)

            if item_found is True:
                option_2 = input("""
                                1-Continue
                                2-Return to menu
                                """)
                if option_2.lower() == "continue" or option_2 == "1":
                    return search(user_type)
                if option_2.lower() == "return to menu" or option_2 == "2":
                    return user_type

            if not item_found:
                print("Item not found...")
                option_2 = input("""
                                1-Continue
                                2-Return to menu
                                """)
                if option_2.lower() == "continue" or option_2 == "1":
                    return search(user_type)
                if option_2.lower() == "return to menu" or option_2 == "2":
                    return user_type



        if (option_1 == "price range") or (option_1) == "4":
            item_found = False
            min_price = int(input("Enter minimum price: "))
            max_price = int(input("Enter maximum price: "))

            for item in inventory:
                if min_price < int(item[0]) and int(item[0]) < max_price:
                    print(item)
                    item_found = True


            if item_found:
                option_4 = input("""
                                1-Continue
                                2-Return to menu
                                """)
                if option_4.lower() == "continue" or option_4 == "1":
                    return search(user_type)
                if option_4.lower() == "return to menu" or option_4 == "2":
                    return user_type

            if not item_found:
                print("Item not found...")
                option_4 = input("""
                                1-Continue
                                2-Return to menu
                                """)
                if option_4.lower() == "continue" or option_4 == "1":
                    return search(user_type)
                if option_4.lower() == "return to menu" or option_4 == "2":
                    return user_type

        if option_1 == "exit" or option_1 == "5":
            return user_type


def admin(user_type):
    while True:
        print('''
                   Please Enter An Option:
                   -----------------------
                   1 - View Inventory
                   2 - Insert Item
                   3 - Delete Item
                   4 - Stock taking
                   5 - Update item
                   6 - View Replenish List
                   7 - Stock Replenishment
                   8 - Search item
                   9 - Add new user
                  10 - Delete user
                  11 - Exit
                   ''')
        choice = input("Enter your option: ")
        if choice == "view inventory".lower() or choice == "1":
            inventory = read_inventory()
            for item in inventory:
                i = ' '.join(item) + '\n'
                print(i)
        if choice == "insert item".lower() or choice == "2":
            item_insert(user_type)
        if choice == "delete item".lower() or choice == "3":
            delete_item(user_type)
        if choice == "stock taking".lower() or choice == "4":
            stock_taking(user_type)
        if choice == "update item".lower() or choice == "5":
            update_inventory(user_type)
        if choice == "View replenish".lower() or choice == "6":
            view_replenish()
        if choice == "stock replenishment".lower() or choice == "7":
            stock_replenishment(user_type)
        if choice == "search item".lower() or choice == "8":
            search(user_type)
        if choice == "add new user".lower() or choice == "9":
            add_new_user(user_type)
        if choice == "delete user".lower() or choice == "10":
            delete_user(user_type)
        if choice == "exit".lower() or choice == "11":
            log_in()


def inventory_checker(user_type):
    while True:
        print('''
        Please Enter An Option:
        ----------------------
        1 - View Inventory
        2 - Stock Taking
        3 - Search item
        4 - Exit
        ''')
        choice = input("Enter your option: ")
        if choice == "view inventory".lower() or choice == "1":
            inventory = read_inventory()
            for item in inventory:
                i = ' '.join(item) + '\n'
                print(i)
        if choice == "stocking taking".lower() or choice == "2":
            stock_taking(user_type)
        if choice == "search item".lower() or choice == "3":
            search(user_type)
        if choice == "exit".lower() or choice == "4":
            log_in()

def purchaser(user_type):
    while True:
        print('''
        Please Enter an Option
        ----------------------
        1 - View Inventory
        2 - Stock Replenishment
        3 - Search item
        4 - Exit
        
        ''')
        choice = input("Enter your option: ")
        if choice.lower() == "view inventory" or choice == "1":
            inventory = read_inventory()
            for item in inventory:
                i = ' '.join(item) + '\n'
                print(i)

        if choice.lower() == "stock replenishment" or choice == "2":
            stock_replenishment(user_type)
        if choice.lower() == "search item" or choice == "3":
            search(user_type)
        if choice.lower() == "exit" or choice == "4":
           log_in()

while True:
    print('''
                Welcome to Main Page
            ---------------------------------
            1 - Log In
            2 - Exit
        ''')
    choice = input("Enter Your Choice: ")
    if choice == '1' or choice == "log in".lower():
        log_in()
    elif choice == '2' or choice == 'Exit':
        break
