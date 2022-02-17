import os
sor = input("For SingUp -> 0\nFor Login -> 1\nPlease choose one: ")
if sor == "0":
    kayt = input("Take username what you want : ")
    if kayt+".txt" in os.listdir():
        print("There is a another user using this username")
    else:
        passw = input("enter your password: ")
        open(kayt+".txt","x")
        dosya = open(kayt+".txt","w")
        dosya.write(passw)
        print("Succesfull")
if sor == "1":
    kadi = input("Username : ")
    if kadi+".txt" in os.listdir():
        sif = input("Password: ")
        dosyar = open(kadi+".txt","r")
        if sif == dosyar.read():
            print("Succesfull")
        else:
            print("Wrong Password for this user")
    else:
        print("There is not user for this nick")