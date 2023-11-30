class stringdemo:
    str= "Angel's birthday"
    print(str)

    str1= 'Tim said, "I\'m busy today"'
    print(str1)
    str_index = str1[4]
    print(str_index)



    #string with multiple lines

    str2 = '''hey there
    how are you?
    where are you?'''
    print(str2)
    length=len(str2)#length of the string
    print(length)

    str3= "Angel"
    for i in str3:
        print(i,end="*")
    print()


    str4 = "Manoj Amirtharaj"
    str4_slice = str4[:5]
    print(str4_slice)
    str4_slice1 = str4[7:]
    print(str4_slice1)
    str4_slice2 = str4[7:10]
    print(str4_slice2)
    print(str4.upper())
    print(str4.lower())
    print(str4.find('raj'))
    print(str4.index('raj'))
    str_list = str4.split()
    print(str_list)
    print(str4.replace('Amirtharaj', 'Angel'))



    str5='Welcome to python tutorial'
    str5_par =str5.rpartition(" to ")
    print(str5_par)

    stg = input("Enter a string")
    stg = stg+" "
    temp = " "
    rev = " "
    for i in stg:
        if i!= " ":
            temp = i+temp
        else:
            rev = rev+temp
            temp = " "
    print(rev)