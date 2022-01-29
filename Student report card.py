#Created by Cyclops!
data = {}

while True :
    nam = input("Enter name : ")
    eng = float(input("Enter English marks : "))
    maths = float(input("Enter maths marks : "))
    cop = float(input("Enter Computer marks : "))
    acc = float(input("Enter accounts marks : "))
    bst = float(input("Enter business marks : "))

    data[nam] = eng,maths,cop,acc,bst
    
    a = input("Do you want to enter more records enter (Y / N):")
    if a == "N" or a == "n":
        break

print (data)
print ("")
las = input("Enter the student you want to search : ")
print(data[las])
