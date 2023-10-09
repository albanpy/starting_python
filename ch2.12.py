#purchase stock details
num_share_purchase=2000
amount_purchase_pershare=40
amount_purchase=num_share_purchase*amount_purchase_pershare
commssion_paid_purchase=amount_purchase*0.03 #commission paid to his stockbroker
#sold stock detail
num_share_sold=2000
amount_sold_pershare=42.75
amount_sold=num_share_sold*amount_sold_pershare
commssion_paid_sold=amount_sold*0.03 #another commission to his stockbroker
#profit
profit=amount_sold-(amount_purchase+commssion_paid_purchase+commssion_paid_sold)

#diplay
print(f'The amount of money Joe paid for the stock=${amount_purchase:,.2f}\n'
      'The amount of commission Joe paid his broker\n'
       f'when he bought the stock=${commssion_paid_purchase:,.2f}\n'
      f'The amount for which Joe sold the stock=${amount_sold:,.2f}\n'
      f'The amount of commission Joe paid his broker\n'
      f'when he sold the stock=${commssion_paid_sold:,.2f}\n'
      'The amount of money that Joe had left when\n'
      f'he sold the stock and paid his broker both timeS=${profit:,.2f}')
      
if profit>=0:
    print("Joe made a profit")
else:
    print("Joe lost money")

