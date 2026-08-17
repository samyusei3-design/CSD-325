#Samuel Guizar
#8/15/26
#Module 1.3 Assignment

#Display numbers of beer bottles until there are none left, then tell user to buy more beer

#Function to countdown number of bottles
def beer_bottles(bottles):

    while bottles > 0:

        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print(f"Take one down and pass it around, {bottles - 1} more bottles of beer on the wall.\n")

        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")

        #Decreases bottles by 1 each time the loop runs
        bottles -= 1

#Asks user for number of bottles and provide error handling
while True:

    try:
        bottles_of_beer = int(input("How many bottles of beer are on the wall? "))

        if bottles_of_beer < 0:
            print("Please enter a number equal to or greater than 0.")
            continue
        break

    except ValueError:
        print("Please enter an integer.")

#Passes input to function
beer_bottles(bottles_of_beer)

#Prints message to remind user to buy more beer
print("You need to buy more beer!")

