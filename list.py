## List

healthy = ["apple", "almonds", "water"]
backpack = ["water", "pizza", "chips", "Banana", "apple"]

healthy.append("waffer") # add to the list
length = len(healthy) # calculate the length of list

if "pasta" in healthy:
    print("Please add the dish")

# Alternative for a loop
backpack[:]= [item for item in backpack if item in healthy] # to check the data in 2 strings and [:] is used that the original list is modified and npt create new list

# Creating the above in loop 
healthy_backpack = []
for item in backpack:
    if item in healthy:
        healthy_backpack.append(item)

squares = [i**2 for i in range(20) if i%2 == 0]

#for i in range(10):
    #squares.append(i**2)


print(squares)

print(healthy_backpack)
print(id(backpack))    
print("Add:", healthy)
print("Length:", length)

# sets don not have duplicateds and uses random order

backpack2 = {"torch", "light", "fan", "tent", "water" }

