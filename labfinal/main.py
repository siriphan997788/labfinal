from function import amount_of_vehicle

input_number = input("Enter the number of passengers: ")
while not input_number.isdigit():
    print("Error: Invalid input.")
    input_number = input("Enter the number of passengers: ")
    
result = amount_of_vehicle(int(input_number))
print(f"{result[0]} van(s) and {result[1]} car(s) are needed to transport {input_number} passengers.")
