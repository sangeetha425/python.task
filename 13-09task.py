def min_max_sum(marks_list):
    if len(marks_list) == 0:
            return 'Invalid list'
    
    min_value=marks_list[0]
    max_value=marks_list[0]
    sum=0
    for i in marks_list:
    
        if i < min_value:
            min_value=i

        if i>max_value:
            max_value=i
       
        sum=sum+i

    print('minimum marks:',min_value)
    print('maximum marks:',max_value)
    print('sum of total marks',sum)
   
list_of_marks=[]
print(min_max_sum(list_of_marks))