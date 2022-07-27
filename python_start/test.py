name_of_list = ['Hello! Have a good day']
new_list = [] 
for i in name_of_list[0][len(name_of_list[0])//2:]:
    new_list.append(i)
    
for i in name_of_list[0][:(len(name_of_list[0]))//2]:
    new_list.append(i)
 
print(new_list)