standin = 0 
checker = 0 
while standin == 0:
    passw = input("enter here: ")
    if len(passw) > 8:
        checker += 1
        print("length is good")
    else: print('that password is not complex ')
    standin += 1
    sp1 = "~!@#$%^&*()_+|}{:><?';./`-=}"
    sp2 = '"'
    sp = sp1 + sp2
    if any(c in sp for c in passw):
        checker += 1
        print("special characters is good ")
    if any(cap.isupper() for cap in passw):
        checker += 1 
        print( "capitalization is good")
    if checker > 3:
        print("password is complex")
    print (checker)
    
