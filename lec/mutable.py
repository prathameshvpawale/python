shopping_list = [ "milk" ,
                 "egg" ,
                 "rice" ,
                 "bread" ,
                 "pasta" ,
                 "banana" ,
                 ]
anather_list = shopping_list
print(id(shopping_list))
print(id(anather_list))
shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(id(anather_list))