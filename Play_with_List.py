L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List :", L)

#Variable to store the sume of
#The list
count = 0

#Finding the sume 
for i in L:
    count += i

#Divide the total elements by
#Number of elements
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

#Sorting the elements of the list
L.sort()

#printing the first element
print ("Smallest element is:", L[0])

#printing the last element
print ("Largest element is:", L[-1])