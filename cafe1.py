# creation of list of items
menu = ["risotto", "chicken alfredo", "antipasti", "lasagne", "garlic bread", "pizza"] 
# creation of first dictionary to show stock levels, linked to menu list
stock = {'risotto': 25,'chicken alfredo': 8, 'antipasti': 15, 'lasagne': 34, 'garlic bread': 18, 'pizza': 28} 
# creation of second dictionary to show prices, linked to menu list
price = {'risotto': 14.50, 'chicken alfredo': 16.50, 'antipasti': 22.00, 'lasagne': 12.28, 'garlic bread': 4.25, 'pizza': 11.00}

total_value = 0
stock_num = 0
for i in menu: # creation of for loop

    total_value = total_value + stock[i] * price[i] # calculation of total value of stock * price per item
print ("Total items in stock:" ,sum(stock.values())) # calculates the sum of the  items in stock
print ()
print ("The total value of the stock is: £" + str(total_value)) # print total_value defined above
# adding for commit