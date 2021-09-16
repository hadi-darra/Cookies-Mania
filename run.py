import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cookies_mania')
STOCK = SHEET.worksheet('stock')
SALES = SHEET.worksheet('sales')
PRICE = SHEET.worksheet('price')


def start():
    """
    Start menu that the user can choose between 6 different tasks.
    """
    print("""
                1. Add new sales\n\
                2. View all stock\n\
                3. View sales\n\
                4. View prices\n\
                5. Reset sales\n\
                6. Exit\n
                    """)
    while True:
        choice = (input("Choose the number of the task you want to do: \n"))
        if choice == '1':
            print("Adding new sales...\n")
            get_sales_data()
            break
        elif choice == '2':
            print("Viewing the current stock...\n")
            view_all_stock()
            break
        elif choice == '3':
            print("Viewing the sales list...\n")
            view_all_sales()
        elif choice == '4':
            print("Viewing the price list...\n")
            view_all_prices()
            break
        elif choice == '5':
            print("Resetting the sales...")
            validate_reset()
            break
        elif choice == '6':
            print("Exit program...")
            exit_program()
            break
        else:
            print("Not a valid input please enter a number 1-6")


def get_sales_data():
    """
    Get sales figures input from the user.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here:\n")

        sales_data = data_str.split(",")
        if validate_data(sales_data):
            print("Data is valid!")
            break

    return update_worksheet_sales(sales_data)


def view_all_prices():
    """
    Function to get prices from google sheet
    and show them as a list
    """
    get_all = SHEET.worksheet("price").get_all_records()
    for price in get_all:
        print_all_price(price)
    back_to_menu()


def print_all_price(existing):
    """
    Function to get prices from google sheet
    and print them on the screen
    """
    all_prices = []
    for name, price in existing.items():
        print(f'{name}: {price}')
    print("-----------------------------------")
    return all_prices


def view_all_stock():
    """
    Function to get the stock from google sheet
    and show them as a list
    """
    get_all = SHEET.worksheet("stock").get_all_records()
    for stock in get_all:
        print_all_stock(stock)
    back_to_menu()


def print_all_stock(existing):
    """
    Function to get the stock from google sheet
    and print them on the screen
    """
    all_stock = []
    for Product, Quantity in existing.items():
        print(f'{Product}: {Quantity}')
    print("-----------------------------------")
    return all_stock


def back_to_menu():
    """
    Instead of get the whole menu after every task, the user get a question if
    he wants to go back to menu or quit.
    """
    while True:
        user_choice = input("Back to menu: M, Quit program: Q \n")
        if user_choice == "M" or user_choice == "m":
            start()
            break
        elif user_choice == "Q" or user_choice == "q":
            exit_program()
        else:
            print("Invalid input, Try again")
            back_to_menu()
            break
        return False


def validate_reset():
    """
    Function make sure that the user want to reset the data
    and asking him for the confirmation
    """
    reset = input("Are you sure you want to reset? Y/N: \n")
    while True:
        if reset == 'Y' or reset == 'y':
            reset_sales()
            break
        elif reset == "N" or reset == "n":
            back_to_menu()
            break
        else:
            print("Not a valid input, Try again!")
            break
        return False


def reset_sales():
    """
    When the user want to reset all stock and delete the worksheet.
    """
    print("delete all sales...\n")
    SALES.clear()
    values = ("Dark Choco and Pistachio", "Salted Dark Choco",
              "Caramel Choco Ship", "Peanut ", "Cranberry")
    new_sheet = SALES.append_row(values)
    print("Sales are now reset")
    back_to_menu()
    return new_sheet


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f"6 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet_sales(sales_data):
    """
    Update sales worksheet, add new row with the list data provided
    """

    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(sales_data)
    print("Sales worksheet updated successfully.\n")
    back_to_menu()


def view_all_sales():
    """
    Function to get all the sales from google sheet
    """
    get_all = SALES.get_all_records()
    for sales in get_all:
        printing_all_sales(sales)
    back_to_menu()


def printing_all_sales(existing):
    """
    Function that print all the existing sales on the screen
    """
    sales = SHEET.worksheet("sales").get_all_values()
    for Product in existing.items():
        print(f'{Product}: ')

    print("-----------------------------------")
    return sales


def exit_program():
    """
    Shutting down program when the user choose the exit task in menu
    """
    print("-------------------------------------------------------")
    print("---------------Thanks for  using POS app---------------")
    print("-------------------------------------------------------")


def main():
    """
    Contains  the start function of the program
    """
    start()


print("   ___            _    _                                      _       ")
print("  / __\___   ___ | | _(_) ___  ___    /\/\   __ _ _ __   __ _(_) __ _ ")
print(" / /  / _ \ / _ \| |/ / |/ _ \/ __|  /    \ / _` | '_ \ / _` | |/ _` |")
print("/ /__| (_) | (_) |   <| |  __/\__ \ / /\/\ \ (_| | | | | (_| | | (_| |")
print("\____/\___/ \___/|_|\_\_|\___||___/ \/    \/\__,_|_| |_|\__,_|_|\__,_|")
print("                                                                      ")
print("-----------------Please choose the number of the service--------------")
print("                                                                      ")
main()
