def checkout(item):
    return(item)

shopping_cart = ['butter', 'milk', 'eggs', 'cheese']

grocery_bag = [checkout(item) for item in shopping_cart]

print(grocery_bag)
