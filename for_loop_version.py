def get_starting_number():
    while True:
        number = input('How many bottles of beer on the wall?')
        if number.isdigit() and int(number) >= 1:
            return int(number)
        else:
            print("Enter a number equal to or greater than 1")

def sing(num_times):
    for i in range(int(num_times), 0, -1):
        if i > 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.\n")
        elif i == 2: 
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
        elif i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")     
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            

