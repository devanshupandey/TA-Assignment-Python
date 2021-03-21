grocery_item = { } 
grocery_history = [ ]
b = input('enter your budget')
stop = False
grand_total = 0
while not stop:
        item_name = input("Enter Product :\n")
        quantity = input("Enter Quantity :\n")
        cost = input("Enter Price :\n")
        grocery_item = {'Product name':item_name,'Quantity':int(quantity),'Price':int(cost)}
        
        for index, item in enumerate(grocery_history):
             item_total = grocery_item['Quantity']*grocery_item['Price']
             grand_total = grand_total + item_total
             if (grand_total > budget):
                 print("item cannot be bought")
             else:
                     grocery_history.append(grocery_item)
        user_input = input("Enter your choice")
        if user_input == '2':
            print(*grocery_history, sep ='\n')
            stop = True
        else:
            stop = False


print(*grocery_history, sep ='\n')
      
