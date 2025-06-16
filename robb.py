#roobing the bank
import random
money = 0
steps = 0
risk = 0
print("You are a robber, and you have 3 steps to rob the bank.")
print("You can choose to rob the bank or leave it alone.")
print("If you rob the bank, you can get money, but you might also get caught.")
print("If you get caught, you will lose all your money and go to jail.")
choice = input(" Enter 'crack' if you want to crack the safe:\n Enter 'robbed' if you want to rob the cash register(but you take less money):\n Enter 'leave' if you want to leave the bank: ").strip().lower()
while True:
    if steps >= 3:
        print("You have been caught by the police! Game over.")
        break
    if choice == "crack":
        print("You try to crack the safe, but it takes time and you lose 1 step.")
        steps += 1
        money += random.randint(10000, 50000)
        print(f"You cracked the safe and got ${money}. Steps left: {3 - steps}")
        choice = input("Enter 'crack' to try again, 'robbed' to rob the cash register, or 'leave' to leave the bank: ").strip().lower()
        if choice == "crack":
            steps += 1
            money += random.randint(10000, 50000)
            print(f"You cracked the safe again and got ${money}. Steps left: {3 - steps}")
            print("You need to leave the bank right now!!!")
            choice = input("Enter 'leave' to leave the bank or 'stay' to stay: ").strip().lower()
            if choice == "stay":
                print("You have been caught by the police! Game over.")
                break
            elif choice == "leave":
                risk = random.randint(0, 1)
                if risk == 0:
                    print("You successfully left the bank with the money.")
                    print(f"You left the bank with ${money}.")
                else:
                    print("You were caught by the police while leaving the bank!")
                    money = 0
                    print("You lost all your money and went to jail.")
                break
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.    
    elif choice == "robbed":
        print("You rob the cash register and get some money, but it's less than cracking the safe.")
        money += random.randint(5000, 15000)
        steps += 1
        print(f"You robbed the cash register and got ${money}. Steps left: {3 - steps}")
        choice = input("Enter 'crack' to try to crack the safe, 'robbed' to rob another cash register again, or 'leave' to leave the bank: ").strip().lower()
        if choice == "crack":
            steps += 1
            money += random.randint(10000, 50000)
            print(f"You cracked the safe and got ${money}. Steps left: {3 - steps}")
            print("You need to leave the bank right now!!!")
            choice = input("Enter 'leave' to leave the bank or 'stay' to stay: ").strip().lower()
            if choice == "stay":
                print("You have been caught by the police! Game over.")
                money = 0
                break
            if choice == "leave":
                risk = random.randint(0, 1)
                if risk == 0:
                    print("You successfully left the bank with the money.")
                    print(f"You left the bank with ${money}.")
                else:
                    print("You were caught by the police while leaving the bank!")
                    money = 0
                    print("You lost all your money and went to jail.")
                break
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
    elif choice == "leave":
        print("You leave the bank without robbing it.")
        print("You didn't get any money, but you also didn't get caught.")
        break
    else:
        print("Invalid choice. Please try again.")
        