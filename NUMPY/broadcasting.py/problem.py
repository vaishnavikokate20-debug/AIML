prices=[100,200,300]
dicount=10
final_prices=[]

for price in prices:
    final_price=price-(price*dicount/100)
    final_prices.append(final_price)
print(final_prices)

