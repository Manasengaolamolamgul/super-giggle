import os
os.system("cls")
name=input("Isimni kiriting: ")
age=int(input("Yoshini kiriting: "))
f=open("ism.txt","w")
if age>0:
    if age%2==0:
        a=f"  {age} Happy birthday {name}! {age}  "
        f.write("#"*len(a))
        f.write(f"# {age} Happy birthday {name}! {age} #")
        f.write("#"*len(a))
    else:
        a=f"  {age} Happy birthday {name}! {age}  "
        f.write("*"*len(a))
        f.write(f"* {age} Happy birthday {name}! {age} *")
        f.write("*"*len(a))