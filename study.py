password = input("enter here: ")
tics = 0 
special1 = ",./';][]\`-=+_)(*&^%$#@!:}{|?><}) "
special2 = '"'
special = special2 + special1

if  len(password) > 8:
    tics += 1 
    print("yes, len")
else: print ("no len")
if password.upper:
    tics += 1
    print("yes. uper")
else: print ("no uper")
if any(c in special for c in password):
    tics += 1 
    print("yes spec")
else: 
    print ("no spec")
if password.isnumeric:
    tics += 1
    print("yes num")
else: 
    print ("no num")
if tics >= 3:
    print(tics)
    print("complex password ")
else:
    print("not complex")
    print(tics)
