#	Write a Python program to accept n numbers in list and remove duplicates from a list

input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
print('list: ', user_list)
for i in range(len(user_list)):
    
    user_list[i] = int(user_list[i])
input_string = list(set(input_string))

print ("The list after removing duplicates : "
        + str(input_string))
