#Built-in functions :List methods (adding,removing,search)
#ADDING
#append -add the element in last of the list.
# list1=[1,2,3,4,5,6,7]
# list1.append(8) #8 will be added to the list above.
# print(list1)

# list1=[1,2,3,4,5]
# list1.append([6,7,8]) #[6,7,8]-considered as single element
# print(list1)

# list1=[1,2,3,4,5,6,7]
# list1.append(8,9) #it won't accept two arguments.
# print(list1)

#extend - adds all the elements of another iterable
# list2=[11,22,33,44]
# list2.extend([55,66,77]) #[55,66,77]-single element but extend spreads them and add to list 
# print(list2)

# list2=[11,22,33,44,55,66,77]
# list2.extend([88]) 
# print(list2)

# list2=[11,22,33,44,55,66]
# list2.extend([77],[88]) #it takes only one argument
# print(list2)

# list2=[11,22,33,44,55,66]
# list2.extend(77) #it doesn't work because extend won't accept arguments if they are not written in square braces
# print(list2)

#Insert (index,element)
# list3=[1,3,5,7,9,11,13,15,17]
# list3.insert(6,15) #6 is index ,15 is the adding element in place of 6 index.
# print(list3)

# list3=[1,3,5,7,9,11]
# list3.insert(5,[13,15,17]) #[13,15,17] considered as one element.
# print(list3)

# list3=[1,3,5,7,9,11]
# list3.insert(3,4,6) #it accepts only two arguments 
# print(list3)

#REMOVING
#clear - it just clear every thing and just print empty list.
# list4=[2,4,6,8,9,10]
# list4.clear()
# print(list4)

# list4=[2,4,6,8,10]
# list4.clear(4) #it takes no arguments
# print(list4)

#pop(index) 
#pop is not a void function it returns the poped value.
# list5=[12,23,34,45,56,67]
# res=list5.pop(3) #stores the return value
# print(res)
# print(list5) #it removes the element with respect to index

# list5=[12,23,34,45,56,67]
# res=list5.pop() #if any index is not given as argument by default pop removes the last element in list.
# print(res)
# print(list5)

# list5=[]
# list5.pop(3) #pop doesn't work on empty list
# print(list5)

# list5=[12,23,34,45,56,67]
# list5.pop(6) #pop index out of range
# print(list5)

#Remove(element)
# list6=[1,2,3,4,5,6,7,8,9]
# list6.remove(5) #remove element 5 from the list
# print(list6)

# list6=[]
# list6.remove(8) #8 is not in the list
# print(list6)

# list6=[1,2,3,4,5,6,7,8,9]
# list6.remove() #remove takes one argument (0 given) 
# print(list6)

# list6=[1,2,2,3,4,5,2,6]
# list6.remove(2) #here it removes only one (2) element from list
# print(list6)

# list6=[1,2,2,3,4,5,2,6]
# list6.remove(2) #First list6.remove(2) removes the first 2
# print(list6)
# for i in range(2):
#     list6.remove(2) #Then the loop removes two more first 2’s one by one.

#Search
#count
# list7=[1,2,3,4,5,6,7,5,8]
# print(list7.count(5)) #it counts how many times the element is repeated in list.

# list7=[1,2,3,4,5,6,7,8]
# print(list7.count(5)) #list.count takes exactly one argument (0 given)

# list7=[1,2,3,4,5,6,7,8]
# print(list7.count(9)) #it gives value (0) when tried to access the number which is not included in list

#index
# list8=[99,88,77,66,55,44,33,22,11]
# print(list8.index(66)) #index gives the index number of a element.

# list8=[99,88,77,66,55,44,33,22,11]
# print(list8.index(77,66)) #77 not in list error 

list8=[99,88,77,66,55,44,33,22,11]
print(list8.index(66,2,8))
