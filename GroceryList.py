#A program to list everything on your grocery list and output the total price
Groc_List = []
Groc_List_Price = 0.00
answer = input("What do you need on your grocery list? Type in the item or type 'End' to end the program.")
while(answer != "End"):
    Groc_List += answer + ","
    price = float(input("What is the cost of this item?"))
    Groc_List_Price += price
    answer = input("What do you need on your grocery list? Type in the item or type 'End' to end the program.")
#print("Items needed:" + str(Groc_List))
print(*Groc_List)
print("Total price: " + str(Groc_List_Price))