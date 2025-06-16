💰 Roobing the Bank

This is a simple text-based console game written in Python where you play as a bank robber. You have 3 steps to make decisions: crack the safe, rob the cash register, or leave the bank before getting caught. But be careful — every action increases your risk of being caught by the police!

🎮 Game Rules

You have 3 steps before the police arrive.
You can choose to:
crack — Crack the safe (high reward, high risk).
robbed — Rob the cash register (lower reward, lower risk).
leave — Leave the bank (no money, but no risk).
If you're caught — you lose all your money and go to jail.
Your decisions affect the outcome of the game. Sometimes it's better to run while you still can!
🧠 Game Logic Example

if choice == "crack":
    # Get a lot of money, but use up a step
elif choice == "robbed":
    # Get less money, but safer
elif choice == "leave":
    # Exit safely with no money
else:
    print("Invalid choice.")
📦 Modules Used

random — to generate random amounts of money and risk of being caught.
✅ How to Run

Make sure you have Python 3 installed.
Download the file roobing_the_bank.py.
Run the script:
python roobing_the_bank.py

