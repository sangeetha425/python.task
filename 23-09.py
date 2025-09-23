list1=[[11,22,33],
       [44,55,66],
       [77,88,99]]

for i in range(len(list1)):
    for j in range(len(list1[i])):
        list1[i][j] = 0
    print(list1)

list1=[[11,22,33],
       [44,55,66],
       [77,88,99]]

for i in range(len(list1)):
    sum=0
    for j in range(len(list1)):
     sum= sum+list1[i][j]
    print(sum)

list1=[[11,22,33],
       [44,55,66],
       [77,88,99]]

for i in range(len(list1)):
    for j in range(len(list1)):
        if i == j:
            list1[i][j] = 0
print(list1)
       
list1=[[11,22,33],
       [44,55,66],
       [77,88,99]]

for i in range(len(list1)):
    j_index=len(list1)-1
    for j in range(len(list1)):
        if j == j_index:
            print(0,end="")
            j_index -= 1
        else:
            print(list1[i][j],end="")
    print()
       