def sorting(mystring):
    
    mystring = mystring.split()
    
    mystring.sort(key=len)
    
    mystring = " ".join(mystring)

    return mystring

x = input("Введите значение")
print(sorting(x))
