from datetime import date

def current_day():
    
    today = date.today()
    wek_Day = today.weekday()

    match wek_Day:
        
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")

current_day()