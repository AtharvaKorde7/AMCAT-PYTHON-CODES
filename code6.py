
init_tuple = ()
print(len(init_tuple))   


init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
print(init_tuple_a == init_tuple_b)


init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print(init_tuple_a == init_tuple_b)


lst = [1, 2, 3]
init_tuple = ('Python',) * (len(lst) - 1)
print(init_tuple)


init_tuple = ('Python') * 3   
print(type(init_tuple))


init_tuple = (1,) * 3
  
print(init_tuple)


init_tuple = ((1, 2),) * 7
print(len(init_tuple[3:8]))