account_balance = 500000
daily_limit = 10000
withdrawal_amount = int(input("Please enter the withdrawal amount: "))
if (withdrawal_amount > daily_limit):
    print("Exceeds daily limit")
elif (withdrawal_amount > account_balance):
    print("insufficient funds")
else :
    print ("success! your remaining balance is :", account_balance - withdrawal_amount)
    