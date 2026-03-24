# Simple ATM Simulation
balance = 1000
print(f"Current Balance: {balance} SEK")

deposit = float(input("Enter amount to deposit: "))
balance += deposit

withdraw = float(input("Enter amount to withdraw: "))
if withdraw <= balance:
    balance -= withdraw
    print(f"Withdrawal successful! New balance: {balance} SEK")
else:
    print("❌ Insufficient funds!")
