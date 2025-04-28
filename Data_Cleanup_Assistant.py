messy_names = [
    "  alice ", "Bob", " charlie", "Alice", "BOB ", "eve  ", " Eve", "eve"]

new_name = [name.strip() for name in messy_names if name.strip().istitle()]
for name in new_name:
    print(name)