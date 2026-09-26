# Python compound interest calculator
name=input("Enter your name: ")
while name=="":
    print(f"{name} is not a valid name")
    name=input("Enter your name: ")
print(f"Welcome {name} to Frankiyung bank ")
p=float(input("Enter the amount you wish to invest in our bank: "))
r=int(input("Enter the rate per year of your money: "))
t=int(input("Enter the no of years you wish to invest: "))
while not(p>0 and r>0 and t>0):
    print("Please re enter a valid amount!!")
    p = int(input("Enter the amount you wish to invest in our bank: "))
    r = int(input("Enter the rate per year of your money: "))
    t = int(input("Enter the no of years you wish to invest: "))
A=p*pow((1+r/100),t)
print(f"Your final amount is {round(A,2)}")



