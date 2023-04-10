'''
Write a python lambda expression for calculating simple interest.
If simple interest is greater than 1000, display as “Platinum Member”, otherwise “Gold Member”.
Use the below formula to calculate the simple interest.
simple_interest=(principal_amount*duration in years*rate_of_interest)/100
'''
principal_amount = int(input("Enter principal amount: "))
year = int(input("Enter duration in years: "))
roi = int(input("Enter rate of interest: "))
print((lambda PA, year, roi: (PA * year * roi) / 100)(principal_amount, year, roi))
x= lambda PA, year, roi: (PA * year * roi) / 100
if x(principal_amount, year, roi) > 1000:
    print("Platinum Member")
else:
    print("Gold Member")


