class CoffeeMachine:
    
    # Ingredient requirement by type of coffee (index: 1 - espresso, 2 - latte, 3 - cappuccino)
    water_cost = [0, 250, 350, 200]
    milk_cost = [0, 0, 75, 100]
    beans_cost = [0, 16, 20, 12]
    
    # How much each type of coffee costs, using the type of coffee as the index
    coffee_cost = [0, 4, 7, 6]
    
    def __init__(self):
        self.current_water = 400
        self.current_milk = 540
        self.current_beans = 120
        self.current_cups = 9
        self.current_money = 550
        self.current_state = "waiting for action"
        self.current_filling_state = "water"
    
    def buy(self, coffee_type):
        if CoffeeMachine.water_cost[coffee_type] > self.current_water:
            print("Sorry, not enough water!")
            print()
            return
        elif CoffeeMachine.milk_cost[coffee_type] > self.current_milk:
            print("Sorry, not enough milk!")
            print()
            return
        elif CoffeeMachine.beans_cost[coffee_type] > self.current_beans:
            print("Sorry, not enough beans!")
            print()
            return
        elif self.current_cups == 0:
            print("Sorry, not enough cups!")
            print()
            return
        print("I have enough resources, making you a coffee!")
        print()
        self.current_water -= CoffeeMachine.water_cost[coffee_type]
        self.current_milk -= CoffeeMachine.milk_cost[coffee_type]
        self.current_beans -= CoffeeMachine.beans_cost[coffee_type]
        self.current_cups -= 1
        self.current_money += CoffeeMachine.coffee_cost[coffee_type]
    
    def take(self):
        print(f"I gave you ${self.current_money}")
        print()
        self.current_money = 0
    
    def print_state(self):
        print("The coffee machine has:")
        print(self.current_water, "of water")
        print(self.current_milk, "of milk")
        print(self.current_beans, "of coffee beans")
        print(self.current_cups, "of disposable cups")
        print(f"${self.current_money} of money")
        print()
    
    def get_current_state_message(self):
        if self.current_state == "waiting for action":
            return "Write action (buy, fill, take, remaining, exit):"
        elif self.current_state == "buying":
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
        elif self.current_state == "filling":
            if self.current_filling_state == "water":
                return "Write how many ml of water do you want to add:"
            elif self.current_filling_state == "milk":
                return "Write how many ml of milk do you want to add:"
            elif self.current_filling_state == "coffee":
                return "Write how many grams of coffee beans do you want to add:"
            elif self.current_filling_state == "cups":
                return "Write how many disposable cups of coffee do you want to add:"
    
    def enter_command(self, command):
        if self.current_state == "waiting for action":
            if command == "buy":
                self.current_state = "buying"
            elif command == "fill":
                self.current_state = "filling"
            elif command == "take":
                self.take()
            elif command == "remaining":
                self.print_state()
        
        elif self.current_state == "buying":
            if command == "back":
                self.current_state = "waiting for action"
            else:
                self.buy(int(command))
                self.current_state = "waiting for action"
        
        elif self.current_state == "filling":
            if self.current_filling_state == "water":
                self.current_water += int(command)
                self.current_filling_state = "milk"
            elif self.current_filling_state == "milk":
                self.current_milk += int(command)
                self.current_filling_state = "coffee"
            elif self.current_filling_state == "coffee":
                self.current_beans += int(command)
                self.current_filling_state = "cups"
            elif self.current_filling_state == "cups":
                self.current_cups += int(command)
                self.current_filling_state = "water"
                self.current_state = "waiting for action"

coffe_machine = CoffeeMachine()

while True:
    command = input(coffe_machine.get_current_state_message())
    print()
    if command == "exit":
        break
    coffe_machine.enter_command(command)
 
