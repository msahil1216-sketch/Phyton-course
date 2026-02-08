#initialize dictionary 
test_dict = {'Codingal' :3, 'is' : 2, 'best' : 2, 'for': 2, 'Coding' : 1}

#Printing original dictionary
print("The original dictionary: " + str(test_dict))

#Intialize value
K = 2

#Using loop
#Selective key value in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

#Printing result
print("Frequency of K is: " + str(res))