l_1 = [1,11,14,5,8,9]
new_list=[]
def less_than_ten(list):
    for value in list:
        if value < 10:
            new_list.append(list)
    return new_list        
less_than_ten(l_1)

l_1 = [1,11,14,5,8,9]
new_list=[]
def less_than_ten(l_1):
    new_list=[i for i in list if i < 10]
    return new_list
less_than_ten(l_1)