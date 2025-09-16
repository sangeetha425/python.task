# list1=[12,33,56,45,34,23]
# for i in range(len(list1)):
#     print([i])

list1=[56,23,45,-10,75,-200]
for j in range(len(list1)-1):
   for i in range(0,len(list1)-1):
         if list1[i] > list1[i+1]:
          list1[i],list1[i+1] = list1[i+1],list1[i]
   print(list1)

list1=[56,23,45,-10,75,-200]
for j in range(len(list1)-1):
    for i in range(0,len(list1)-1):
        if list1[i] < list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
    print(list1)


str1=input('enter a string:')
char_list=list(str1)
for i in range(len(char_list)-1):
    for j in range(len(char_list)-1):
        if char_list[j] > char_list[j+1]:
            char_list[j],char_list[j+1] = char_list[j+1],char_list[j]
    print(char_list)
print("".join(char_list))

#Running maximum of each innerlist
lst=[[1,2,3],[6,5,4],[-9,10,6],[7,8,9]]
new_list=[]
for i in lst:
    max_val=i[0]
    for j in i:
        if j > max_val:
            max_val = j
    new_list.append(max_val)
print(new_list) 

str1=["namsate","ela unnav","bagunnava","hi","hello",]
for i in range(len(str1)-1):
    for j in range(len(str1)-1):
        if len(str1[j]) > len(str1[j+1]):
          str1[j],str1[j+1] = str1[j+1],str1[j]
    print(str1)