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

def start():
    """
    Start menu that the user can choose between 6 different tasks.
    """
    print("""
                1. Add new sales\n\
                2. View all stock\n\
                3. View sales\n\
                4. View prices\n\
                5. Reset stock\n\
                6. Exit\n
                    """)
    while True:
        choise = (input("Choose the number of the task you want to do: \n"))
        if choise == '1':
            print("Taking you to Go Add new sales...\n")
            get_sales_data()
            break
        elif choise == '2':
            print("Taking you to Open the stock...\n")
            show_all_contacts()
            break
        elif choise == '3':
            print("Taking you to Delete a contact...\n")
            delete_menu()
        elif choise == '4':
            print("Taking you to Search menu...\n")
            search_contact()
            break
        elif choise == '5':
            print("Taking you to Reset stock...")
            validate_reset()
            break
        elif choise == '6':
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
    return sales_data

def back_to_menu():
    """
    Instead of get the whole menu after every task, user get a question if
    they want to go back to menu or quit.
    """
    while True:
        user_choise = input("Back to menu: M, Quit program: Q \n")
        if user_choise == "M" or user_choise == "m":
            start()
            break
        elif user_choise == "Q" or user_choise == "q":
            exit_program()
        else:
            print("Invalid input, Try again")
            back_to_menu()
            break
        return False

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data

def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("sales")
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])

    return columns

def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data

def exit_program():
    """
    Shutting down programme when user choose the exit task in menu
    """
    print("-------------------------------------------------------")
    print("---------------Thanks for  using POS app---------------")
    print("-------------------------------------------------------")

def main():
    """
    contains all the functions for the program
    """
    start()
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "stock")
    """

print("   ___            _    _                                      _       ")
print("  / __\___   ___ | | _(_) ___  ___    /\/\   __ _ _ __   __ _(_) __ _ ")
print(" / /  / _ \ / _ \| |/ / |/ _ \/ __|  /    \ / _` | '_ \ / _` | |/ _` |")
print("/ /__| (_) | (_) |   <| |  __/\__ \ / /\/\ \ (_| | | | | (_| | | (_| |")
print("\____/\___/ \___/|_|\_\_|\___||___/ \/    \/\__,_|_| |_|\__,_|_|\__,_|")
print("                                                                      ")
print("-----------------Please choose the number of the service--------------")
print("                                                                      ")
main()

