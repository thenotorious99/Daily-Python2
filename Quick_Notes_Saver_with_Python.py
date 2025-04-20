text = input("Write a note: ")
with open("notes.txt", "w") as file:
    file.write(text)
    print("Note saved!")