day = input("Enter day:")
match day:
    case  "Monday":
        print("Today is Monday")
    case "Tuesday":
        print("Today is Tuesday")
    case "Wednesday":
        print("Today is Wednesday")
    case _:
        print("Today is not Monday, Tuesday, or Wednesday")
