"""
Erick Gonzalez Cruz
File: This is to practice my knowledge of arrays!!!
"""

#Original array
list_ex = [1, 2, 4, 8]
print(list_ex)
print("-" * 100)

#Inserting a number to my array!
list_ex.insert(2, 3) #(the index I want to add it too, the value I want in my index)
#In this case im inserting 3 to the 3rd index value! 
print(list_ex)
print("-" * 100)

#deleting an index 
list_ex.pop(2)#I delete the three I added earlier because its in the index 2 spot
print(list_ex)
print("-" * 100)

#Updating an index
list_ex[0] = 30 #replacing index 0 (So instead of a 1 I put in 30) 
print(list_ex)
print("-" * 100)

#Traversing the array
for i in list_ex:
    print(i)
print("-" * 100)

#Reversing an array 
list_1 = [1, 2 , 3, 4]
print(list_1)

start = 0
end = len(list_1) - 1 #This will give the lst index of an array 

while start < end: 
    list_1[start], list_1[end] = list_1[end], list_1[start] #Sqapping the indexs 
    start += 1 #Move the start index one step forward
    end -= 1 #Move the end index one step backwards 

print(list_1)



