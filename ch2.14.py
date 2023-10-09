P=float(input("The amount of principal originally deposited into the account:"))
r=float(input("The annual interest rate paid by the account:"))
n=int(input("The number of times per year that the interest is compounded:"))
t=int(input("The number of years the account will be left to earn interest:"))
#r interest rate in percentage like 2 not .02
A=P*(1+r/n)**n*t
#print('The amount of money that will be in the account\n'
      #f'after the specified number of years={A:,.2f}')
print(f'The amount of money that will be in the account after {t} years=Tsh {A:,.2f}')
