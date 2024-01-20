# type conversion
# int(num_str)
# to_numeric
# to_datetime
# astype

############### LIST ###############
my_list_str = ['bat','bold','suren','gerel','chimeg','sar','nar','od']
my_list_str[2]     # 3rd element
my_list_str[:1]    # 0th element
my_list_str[:2]    # 0 and 1st element
my_list_str[1:]    # 1 and up to last element
my_list_str[::-1]  # reverse list 
my_list_str[::-2]  # reverse list, but every second element starting from the last
my_list_str[-1]    # last element
my_list_str[-2]    # second to the last element


# any elements possible
my_list_num = [15, 15.2, 4.7]
type(my_list_num)

my_list_mix = [15, 15.2, 'hello']
type(my_list_mix)


# join elements
txt = ['Suren', 'Dorj', 'Borjigin']
",".join(txt)
" ".join(['Suren', 'Dorj', 'Borjigin'])
"".join(['Suren', 'Dorj', 'Borjigin']) 
"___a___".join(['Suren', 'Dorj', 'Borjigin'])


# append list
my_list_str.append('altan')

# insert into list
my_list_str.insert(2, "orange")

# extend list
bchh = ["delger", "bayar", "urlee"]
my_list_str.append(bchh)
my_list_str.extend(bchh)



# remove by index
my_list_str.pop()  # last item
my_list_str.pop(2) # second item
# or
del my_list_str[5]
del my_list_str[3:5]

# remove by value
my_list_str.remove('bat')

my_list_str[2] = 'mungun'

############### TUPLE ###############

# tuple - just list, but immutable
my_tuple = (1,2,3)
my_list = list(my_tuple)
tuple(my_list)
my_tuple[2] = 10 


############### SET ###############
my_set = {1,2,3}
# my_set[2] # can not do this
my_set.add(10)
my_set.add(2)
my_set.add(0)
my_set.add(-5)

my_set.update([2, 3, 4])
my_set.update([4, 5], {1, 6, 8})
my_set.discard(4) # no error if missing
# my_set.remove(4)  # error if missing
my_set.remove(5)  # error if missing
my_set.pop() # drop first, show it on console

my_list = [1,1,1,1,2,2,3]
my_set = set(my_list)


# traditional set operations
my_set = {1,2,3}
my_set2 = {1,2,7,8,9}
my_set | my_set2 # join |
my_set & my_set2 # intersection &
my_set2 - my_set

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)
A.union(B)
B.union(A)

print(A & B)
A.intersection(B)
B.intersection(A)

print(A - B)
A.difference(B)
print(B - A)
B.difference(A)



############### DICTIONARY ###############

my_husband = {"name": "Bat", "age":25,"country":"Mongolia"} # JSON 
type(my_husband)

my_husband['age'] 
my_husband.get('age')
my_husband['age'] = 27
my_husband['address'] = 'Downtown'

person2 = {"name": "Bold", "age": 50,"country": "Mongolia","city": "Darkhan"}
big_dict = {"Younger": my_husband, "Older": person2}
big_dict['Younger']
big_dict['Younger']['name']

my_husband.keys()
my_husband.values()
list(my_husband.keys())
list(my_husband.values())

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squares[5]
squares.pop(4) # drop key with value 4

'Python'
print('Python with print')