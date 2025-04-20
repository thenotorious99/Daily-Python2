import random

choose = input("Choose your workout type "
               "(cardio/strength/flexibility):")

strength = ["Push-ups", "Squats", "Lunges", "Plank", "Dumbbell Press"]
cardio = ["Jumping Jacks", "Burpees", "Running in Place", "Jump Rope", "High Knees"]
flexibility = ["Yoga Stretch", "Hamstring Stretch", "Toe Touches", "Cat-Cow Stretch", "Shoulder Rolls"]

if choose == "strength":
    print(f"Try this exercise: {random.choice(strength)}")
    print("Stay active and keep moving!")
if choose == "cardio":
    print(f"Try this exercise: {random.choice(cardio)}")
    print("Stay active and keep moving!")
if choose == "flexibility":
    print(f"Try this exercise: {random.choice(flexibility)}")
    print("Stay active and keep moving!")

