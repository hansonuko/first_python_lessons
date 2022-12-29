mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

#print lists 1,2,3
print(mylist[0])
print(mylist[1])
print(mylist[2])

# or another shorter way to print the list
for x in mylist:
    print(x)

mylist2 = [10,15,20]

numbers = []
strings = []
names = ["Comfort", "Uko", "David"]

numbers.append(5)
numbers.append(6)
numbers.append(7)
print(numbers) #prints 5,6,7 in array

strings.append("hello")
strings.append("world")
print(strings)

second_name = names[1] # access the second name from the list in the array

print("The second name on the name is %s" % second_name)