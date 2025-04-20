import random

breakfast_options = ["Oatmeal with fruits", "Scrambled eggs and toast", "Smoothie bowl", "Greek yogurt with granola"]
lunch_options = ["Grilled chicken salad", "Quinoa with roasted veggies", "Spaghetti with tomato sauce", "Sushi rolls"]
dinner_options = ["Baked salmon with rice", "Vegetable stir-fry", "Chickpea curry", "Tacos with beans and avocado"]

print("Welcome to the Meal Planner Assistant!")

# Izpolzvame random zashtoto pravi neshta na sluchaen princip
print(f"Breakfast: {random.choice(breakfast_options)}")
print(f"Lunch: {random.choice(lunch_options)}")
print(f"Dinner: {random.choice(dinner_options)}")

print("Enjoy your meals and eat healthy!")

