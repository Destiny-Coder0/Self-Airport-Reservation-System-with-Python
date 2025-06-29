class orderingFood:

  def __init__(self):
    self.menu = {
      '1' : {'food': 'Pizza', 'price': 30},
      '2' : {'food': 'Burger', 'price': 20},
      '3' : {'food': 'Fried Chicken', 'price': 25},
      '4' : {'food': 'Hot Dog', 'price': 10},
      '5' : {'food': 'Taco', 'price': 15},
      '6' : {'food': 'French Fries', 'price': 5},
      '7' : {'food': 'Onion Rings', 'price': 5},
      '8' : {'food': 'Ayran', 'price': 3},
      '9' : {'food': 'Cola', 'price': 5},
      '10' : {'food': 'Water', 'price': 1} }

    self.orderList = [] #Empty order list.

  def showMenu(self):
    print('\nMenu: \n')
    for x,y in self.menu.items():
      print(x+ "." + str(y['food'])+ ' --> '+ str(y['price'])+ ' TL')


  def addOrder(self,foodNo,quantity):   

    food = self.menu.get(foodNo)
    if food:
      totalOne= food['price'] * int(quantity) #Total price of one item
      food['quantity'] = int(quantity)
      food['totalOne'] = totalOne  #I included it in the 'food' dictionary
      self.orderList.append(food) #Append is an adding function for a list
      print(str(quantity) + ' ' + str(food['food']) + ' added to your order list.') 

    else:
      print('Invalid number.')




  def totalPrice(self):
    total = sum(order['totalOne'] for order in self.orderList)
    print('Total price: ' + str(total) + ' TL')
    return total

  def showOrder(self):

    print('Order list: \n')
    for order in self.orderList:
      print(str(order['quantity']) + ' ' + str(order['food']) + ' - Total Price: ' + str(order['totalOne']) + ' TL')


if __name__ == "__main__":
  orderingProgram = orderingFood()

  while True:
    print(' ')
    print('1. Show the menu.')
    print('2. Add order.')
    print('3. Show order.')
    print('4. Show the total price.')
    print('5. Exit.')

    choice= input('Enter a number between 1-5: ')

    if choice == '1':
      orderingProgram.showMenu()
    elif choice == '2':
      foodNo= input('Enter food number: ')
      quantity= input('Enter the quantity you want to order: ')
      orderingProgram.addOrder(foodNo,quantity)

    elif choice== '3':
      orderingProgram.showOrder()
    elif choice== '4':
      orderingProgram.totalPrice()
    elif choice== '5':
      print('Exiting... Thank you for choosing us!')
      break
    else:
      print('Invalid number.')