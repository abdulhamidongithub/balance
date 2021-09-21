import sys
from sqlite3 import connect
import time

# with connect("balance.db") as db:
#     cursor = db.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE balance(
#             money DECIMAL(10, 5)
#         )
#         """
#     )

if len(sys.argv) != 2:
    sys.exit("You've made a mistake in input!")
orders = ["earned", "spent", "balance"]
order = sys.argv[1]
if order not in orders:
    print("No this type of order option!")
else:
    with connect("balance.db") as db:
        cursor = db.cursor()
        if order == 'earned':
            earned_money = float(input("Enter the money you earned: "))
            cursor.execute(
                """
                INSERT INTO balance(money)
                VALUES(?)
                """, (earned_money,)
            )
            print("Updating the balance...")
            time.sleep(2)
            print("Your balance is updated!")
            cursor.execute(
                """
                SELECT sum(money) from balance
                """
            )
            my_balance = cursor.fetchone()
            print(f"Your balance is: {my_balance[0]}$")
        elif order == "spent":
            money_spent = float(input("Enter the money you spent: "))
            money_spent = -1 * money_spent
            cursor.execute(
                """
                INSERT INTO balance(money)
                VALUES(?)
                """, (money_spent,)
            )
            print("Updating the balance...")
            time.sleep(2)
            print("Your balance is updated!")
            cursor.execute(
                """
                SELECT sum(money) from balance
                """
            )
            my_balance = cursor.fetchone()
            print(f"Your balance is: {my_balance[0]}$")
        elif order == "balance":
            cursor.execute(
                """
                SELECT sum(money) from balance
                """
            )
            my_balance = cursor.fetchone()
            print(f"Your balance is: {my_balance[0]}$")


