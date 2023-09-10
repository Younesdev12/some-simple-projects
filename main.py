import os
import time
while 1:
    print("1 - calculator : simple calculator\n2 - CC number hide : hides first 12 numbers of a credit card number\n3 - discount calculator : calculates discount when applied\n4 - flip a coin : heads or tails\n5 - Vowels & Consonants counter\n6 - XsOs : checks if the Xs are equal to the Os in the senstence")
    choice = input(" : ")
    if choice == "1":
        os.startfile("src\calculator.py")
        break
    elif choice == "2":
        os.startfile("src\ccnumberhide.py")
        break
    elif choice == "3":
        os.startfile("src\discountcalculator.py")
        break
    elif choice == "4":
        os.startfile("src\coinflip.py")
        break
    elif choice == "5":
        os.startfile("src\Vowel_Consonants_counter.py")  
        break
    elif choice == "6":
        os.startfile("src\Xs&Os.py")
        break
    else:
        print("choose a valid choice!")
        time.sleep(2)

    
