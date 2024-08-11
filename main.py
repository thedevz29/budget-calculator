expenses = []
def add(am,cat):
    expense = {'amount':am,'category':cat}
    expenses.append(expense)
    
def prtmenu():
    print("Please chose from the below options: ")
    print("1, Add expense")
    print("2. Print expenses")
    print("3. Exit the app")
def listexpense():
    print("Your expenses are: ")
    print("=============================")
count = 1
for expense in expenses:
    print("  ",count,".     - ",expense["amount"]," - ",expense["category"])
    
if __name__ == "__main__":
    while True :
        prtmenu()
        x = input("Enter your choice: ")
        if x == "1":
            y=  input("Enter the expense category: ")
            z= float(input("Enter the expense amount: "))
            add(y,z)
        elif x == "2":
            listexpense()
        elif x == "3":
            break
        else:
            print("WRONG CHOICE")
