def flatten(lst):
    #Flattens a list of lists and/or tuples.
    
    flat_lst = []
    
    def flat(lst):
        for e in lst:
            if type(e) == list or type(e) == tuple:
                flat(e)
            else:
                flat_lst.append(e)
    
    flat(lst)    
    return flat_lst

#Tests
'''
my_list = [[1,5, [3,'4', (5,6), 5], 8], 5, 10]

my_flat_list = flatten(my_list)       
print(my_flat_list.count(5))
print('flattened list:', my_flat_list)
print(my_list)
print(flatten(my_list).count('4'))
print(my_list)
'''
