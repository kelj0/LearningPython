def total(a,*numbers,**phonebook):
    print('a',a)

    for single_number in numbers:
        print("Single_number ", single_number)
    
    for first_part,second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1234,Nibba=4321,Ingde=1560))