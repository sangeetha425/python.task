#sum of digits of the numbers given in a list
list1=[123,456,789]
dlist=[]
for n in list1:
    sum=0
    while n!=0:
        digit=n%10
        sum=sum+digit
        n=n//10
    dlist.append(sum)
print(dlist)

#maximum digit in a given number
n=int(input('enter a value:'))
list1=[]
while n!=0:
      digit=n%10
      list1.append(digit)
      n=n//10
      max=list1[0]
      for i in list1:
          if i > max:
              max=i
print(max)

# #maximum digit  of a number given in list
list1=[123,456,789]
new_list=[]
dlist=[]
for n in list1:
    while n!=0:
        digit=n%10
        dlist.append(digit)
        n=n//10
    max=dlist[0]
    for x in dlist:
        if x>max:
            max=x
    new_list.append(max)
print(new_list)