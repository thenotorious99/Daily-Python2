import datetime

festivals = {
    "Diwali": "11-01",
    "Holi": "03-25",
    "Navratri": "10-03",
    "Raksha Bandhan": "08-19",
    "Eid": "04-10",
    "Pongal": "01-14",
}

def str_to_date(date_str):
    return datetime.datetime.strptime(date_str, "%m-%d")

today = datetime.datetime.now()

upcoming_festivals = [
    festival for festival, date in festivals.items() if str_to_date(date) > today]

if upcoming_festivals:
    next_festival = min(upcoming_festivals, key=lambda  festival: str_to_date(festivals[festival]))
    print(f"Next Festival is {next_festival} on {festivals[next_festival]}")
else:
    print("Doesn't have festival today")




