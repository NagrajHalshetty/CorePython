from itertools import count


str1 = "nagrajhalshetty"

# length of string
print(len(str1))

# string count
print(str1.count("a"))

# string slicing
print(str1[slice(6)])

# swaping first and last charecter
swap = "nagraj halshetty"
start = swap[0]
end  = swap[-1]

swapstring = end + swap[1:-1] + start
print(swapstring)

# Remove odd index values

name = "nagrajhalshetty"
name2 = []
for i in range(len(name)):
    if i % 2 != 0 :
        name2.append(name[i])
    
print(name2)

str1 = 'This is a String'
print(str1)
print("Printing the first character of str1 "+str1[0])
print("Printing the first word of str1 "+str1[0:4])