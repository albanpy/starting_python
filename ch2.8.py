charge_amount=int(input("Enter the charge for the food:"))
amount_tip=charge_amount*0.18
sales_tax=charge_amount*0.07
total_amount=charge_amount+amount_tip+sales_tax
print(f"Amount of charge for the food={charge_amount:,}")
print(f"Amount of a 18 percent tip={amount_tip:,.2f}")
print(f"Amount of 7 percent sales tax={sales_tax:,.2f}")
print(f"Amount of a meal purchased={total_amount:,.2f}")
