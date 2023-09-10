import os
os.system("title CC number hide")
def hider():
    def result():
        target = x[0:11]
        result = x.replace(target, "xxxxxxxxxxxx")
        print(result)
    def smallnum():
        print("must be 16 digits or higher!")
    def invalid():
        print("must be a number!")

    if x.isdigit():
        if len(x) >= 16:
            result()
        else:
            smallnum()   
    else:
        invalid()
while 1: 
    x = input("Enter the number : ")
    hider()

