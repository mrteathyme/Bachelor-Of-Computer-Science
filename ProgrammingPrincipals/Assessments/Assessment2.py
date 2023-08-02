milk = 1000
coffee = 1000

while milk > 0 and coffee > 0:
    print(f"Welcome!\n\nCoffee remaining: {coffee}\nMilk remaining: {milk}\n")
    drink_choice = input("Coffee Type:\n\n[1] Latte\n[2] Cappucino\n[3] Espresso\n\nEnter Choice: ")
    #I wouldve preferred to use an array of ratios here instead of magic numbers and just index into it but we havnt covered that yet
    if drink_choice == "1":
        milk_ratio = 0.5
        coffee_ratio = 0.5
    elif drink_choice == "2":
        milk_ratio - 0.25
        cofee_ratio = 0.75
    elif drink_choice == "3":
        milk_ratio = 0.0
        coffee_ratio = 1.0
    else:
        #Handling unexpected user input
        print("Invalid Choice")
        continue

    drink_size = input("Size:\n\n[1] Small\n[2] Large\n\nEnter Choice: ")
    #Same deal with the array here
    if drink_size == "1":
        cost = 3
        volume = 200
    elif drink_size == "2":
        cost = 5
        volume = 400
    else:
        #Handling unexpected user input again
        print("Invalid Choice")
        continue

    milk_used = volume * milk_ratio
    coffee_used = volume * coffee_ratio

    if milk - milk_used < 0 or coffee - coffee_used < 0:
        print("Insufficient Ingredients")
        break

    milk -= milk_used
    coffee -= coffee_used

    #Formatted this to be a bit more readable, functionally doesnt change anything
    print(f"""
Ingredients

 Coffee : {coffee_used} ml
 Milk   : {milk_used} ml

Cost: ${cost}\n      
    """)
    input("Press Enter to continue...")

print("\n\nWere all out of Ingrediens\nPlease come again")
