
def amount_of_vehicle(number):
    if not isinstance(number, int):
        return ("Input must be an integer")  
    if number < 0:
        return ("Input must be a non-negative integer")  
    if number == 0:
        return ("No vehicle needed")  
    
    van = number // 11
    remaining_passengers = number % 11  
    if remaining_passengers == 0:
        return (f"{van} van(s) needed")
    elif number < 11:
        car = (remaining_passengers + 3) // 4
        return (f"{car} car(s) needed")
    else:
        car = (remaining_passengers + 3) // 4
        return (f"{van} van(s) and {car} car(s) needed")