import os
import time
os.system("title Are the Xs equal to the Os?")
while 1:
    p = input("Enter the word/sentence : ")
    Os = 0
    Xs = 0
    for i in p:
        if i in "o":
            Os+=1
        if i in "x":
            Xs+=1   
    if Xs == Os:
        os.system('cls')
        os.system("color a")
        print(True)
        time.sleep(2)
        os.system('cls')
        os.system("color 7")  
    else:
        os.system('cls')
        os.system("color 4")
        print(False)
        time.sleep(2)
        os.system('cls')
        os.system("color 7")    
