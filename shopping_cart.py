import datetime

today = datetime.date.today()

now = datetime.datetime.now()



products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

product_ids = []

while True:
    product_id = input("Hey! Please insert the number ID of your product for purchase: ")
    if product_id == "DONE":
        break
    else:
        product_ids.append(int(product_id))


running_total_price = 0

print("--------------------")
print("Singh's Health Food Grocery & Neighborhood Market")
print("--------------------")
print("Web: www.singhsgrocery.com")
print("Phone: 212-555-5555")
print('Checkout time: ' + '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)) #learned how to do variable substitution from Codecademy
print("--------------------")


print("PURCHASED ITEMS:")
for product_id in product_ids:
    matching_products = [product for product in products if product["id"] == product_id]
    matching_product = matching_products[0]
    running_total_price += matching_product["price"]
    price_usd = ' ${0:.2f}'.format(matching_product["price"])
    print(' + ' + matching_product["name"] + price_usd)
#Refenced your YouTube video for the proper way to do the list comprehension formula

running_total_price_usd = ' ${0:.2f}'.format(running_total_price)
print("--------------------")
print("SUBTOTAL: " + running_total_price_usd)

tax = running_total_price * .08875
tax_usd = ' ${0:.2f}'.format(tax)
print("NYC SALES TAX: " + tax_usd)

total_price = running_total_price + tax
total_price_usd = ' ${0:.2f}'.format(total_price)
print("TOTAL PRICE: " + total_price_usd)

print("--------------------")
print("We hope that you enjoyed shopping at our store. Thanks and have a great day!")
print("--------------------")
