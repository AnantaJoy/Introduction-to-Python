weeks = ["Friday", "Saturday", "Sunday", "Monday"]

for weekday in weeks:
    # print(weekday)
    if weekday == "Friday" or weekday == "Saturday":
        print("Weekend")
    else:
        print("Working day")