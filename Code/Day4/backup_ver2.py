def string_splosion(str):
    counter=1
    for i in str:
        print(str[0:counter],end='')
        counter+=1
string_splosion('Code')