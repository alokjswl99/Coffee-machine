from data import MENU, resources

def check_resources(coffee,ingredients):
    insufficient=[]
    for items in MENU[coffee]["ingredients"]:
        if ingredients[items] < MENU[coffee]["ingredients"][items]:
            insufficient.append(items)
    return insufficient

def reduce_resources(coffee,remaining):
    for items in MENU[coffee]["ingredients"]:
        remaining[items]-=MENU[coffee]["ingredients"][items]
    return remaining
remaining_resource=resources.copy()
more_coffee=True
balance=0

while more_coffee:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    which_coffee=input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if which_coffee=='off':
        more_coffee=False

    # TODO: 3. Print report.
    elif which_coffee=="report":
        print(f"Water: {remaining_resource['water']}\nMilk: {remaining_resource['milk']}\nCoffee: {remaining_resource['coffee']}\nMoney: ${balance}")

    # TODO: 8. Refill
    elif which_coffee=="refill":
        remaining_resource=dict(resources)
        print("Ingredients Refilled.")

    # TODO: 4. Check resources sufficient?
    elif which_coffee=="espresso" or which_coffee=="latte" or which_coffee=="cappuccino":
        report=check_resources(which_coffee,remaining_resource)
        if report:
            for n in range(len(report)):
                print(f"There is not enough {report[n]}.")
        else:
            # TODO: 5. Process coins.
            print("Please insert coins.")
            quarters=int(input("How many quarters?:"))
            dimes=int(input("How many dimes?:"))
            nickels=int(input("How many nickels?:"))
            pennies=int(input("How many pennies?:"))
            total=round((quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01),2)
            # TODO: 6. Check transaction successful?
            if total<MENU[which_coffee]["cost"]:
                print(f"Sorry that's not enough money. Put more ${round(MENU[which_coffee]['cost']-total,2)}. Money refunded: ${total}.")
            elif total==MENU[which_coffee]["cost"]:
                # TODO: 7. Make Coffee.
                print(f"Here is your {which_coffee}. Enjoy!")
                remaining_resource=reduce_resources(which_coffee,remaining_resource)
                balance+=MENU[which_coffee]["cost"]
            else:
                # TODO: 7. Make Coffee.
                refund=round(total-MENU[which_coffee]["cost"],2)
                print(f"Here is ${refund} dollars in change.")
                print(f"Here is your {which_coffee}. Enjoy!")
                remaining_resource=reduce_resources(which_coffee,remaining_resource)
                balance+=MENU[which_coffee]["cost"]
