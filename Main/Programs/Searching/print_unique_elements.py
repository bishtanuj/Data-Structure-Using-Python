# Program to print the unique elements of string

# Scan the length of string
string_length = int(input("Enter the length of string: "))

# Scan the string
string = input(f"Enter the string of length {string_length}: ")[:string_length]

# Declare the List
unique_element_list = []

# Append the list with the unique elements of string
for i in range(string_length):
    if string[i] not in unique_element_list:
        unique_element_list.append(string[i])

# Print the unique elements of string
count = 0
print("Unique Elements: ", end="")
for i in range(len(unique_element_list)-1):
    print(unique_element_list[i], end=",")
    count += 1
print(unique_element_list[count])

    
```
OUTPUT 1:
Enter the length of string: 6
Enter the string of length 6: aabcde
Unique Elements: a,b,c,d,e
  
OUTPUT 2:
Enter the length of string: 6
Enter the string of length 6: 12er56
Unique Elements: 1,2,e,r,5,6
```
