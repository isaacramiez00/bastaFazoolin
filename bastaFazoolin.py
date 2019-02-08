#bastaFazoolin CA project
#credits to CodeAcademy

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "This is the {name} menu. This menu is available from {start_time} to {end_time}.".format(name = self.name, start_time = self.start_time, end_time = self.end_time)

    #purchased_items is a list
    def calculate_bill(self, purchased_items):
      total_price = 0
      #for pItem in purchased_items:
      for pItem in purchased_items:
        if pItem in self.items:
          total_price += self.items.get(pItem)
      return total_price

class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    # menus is a list 

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available_menus.append(menu)

    return available_menus
    
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11.00, 16.00)

early_bird = Menu("Early-bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15.00, 18.00)

dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17.00, 23.00)

kids = Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11.00, 21.00)

arepas_menu = Menu("Take a' Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10.00, 20.00)

menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

business_1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
business_2 = Business("take a' Arepa", arepas_place)


#executes: "This is the Brunch menu. This menu is available from 11:00 to 16:00."
#print(brunch)

#13.5
#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

#print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
#21.5 


#output: returns the address
#print(flagship_store, new_installment)

#executes the available menus: [early_bird, dinner, and kids] menu
# print(flagship_store.available_menus(18.00))

print(business_1.name)