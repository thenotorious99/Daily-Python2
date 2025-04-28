shopping_list = ["apples", "bananas", "oranges", "milk", "bananas", "bread", "apples"]

print("Organized Shopping List:")
shopping_list.sort()

for shopping in shopping_list:
    print(f"-{shopping.capitalize()}")