firstContent = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
print(firstContent)

ourMenu = ['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']
ordersList = []
i = True
while i:

    if len(ordersList):
        print('      ***************      ')
        print('')
        print('')
        print('')
        print('If you have anothr order type it or type quit to exit ???')
    
    yourOrder = input()

    if yourOrder in ourMenu:
        ordersList.append(yourOrder)
        
        x = ordersList.count(yourOrder)
            
        print(f"** {x} order of {yourOrder} have been added to your meal **")



    elif yourOrder == 'quit':
        break


    else:
        print('your order not from the menu .... try again :( ')    
