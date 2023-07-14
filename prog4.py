#Write a Python program to print average of all elements of sets.
tup={4,5,1,2,9,7,10,8} 
count=0 
for i in tup: 
    count+=i 
    avg=count/len(tup) 
print("Given tuple :",tup)
print("average :",avg) 
