#1. Write program to get result below
# using nested_forloop
# [ 
    # {1:2,2:4,3:6 ........ 49:98},
    # {1:100,2:104,3:106 ........ 49:198},
    # {1:200,2:204,3:206 ........ 49:298}
# ]
x = [] # empty list
b= 1
for i in range(0,3): # getting one by one 0 ,1,2
    y = {}           #empty dect
    x.append(y)      #[{},{},{}]
    if (i < 1):      # i=0
       index= 1        
    else:
        index = i*100+1 #i= 1,2 (101, 201)
    for a in range(index,100+index): #(101,201)  (201,301)
        if (a%2 != 0 ):
            continue
        y.update({b:a}) 
        b+=1
    x[i] = y
print (x)


"""
result = [] # empty list
dict_key=1
for list_index in range(0,3): # getting one by one 0 ,1,2
    num_dict = {}           #empty dect
    result.append(num_dict)      #[{},{},{}]
    if (list_index < 1):      # i=0
       for_loop_index_start= 1        
    else:
        for_loop_index_start = list_index*100+1 #i= 1,2 (101, 201)
    for_loop_index_stop=100+for_loop_index_start
    for each_num in range(for_loop_index_start,for_loop_index_stop): #(1,101)(101,201) (201,301)
        if (each_num %2 != 0 ):
            continue
        num_dict.update({dict_key:each_num }) 
        dict_key+=1
    result [list_index] = num_dict
print (result )

"""