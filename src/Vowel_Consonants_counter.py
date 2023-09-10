import os
os.system('title Vowels and Consonants counter')
user_input = input("Enter the word/sentence : ")
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
def counter():
    vowels_count = 0
    consonants_count = 0
    for i in user_input:
        if i in vowels:
            vowels_count+=1  
    for i in user_input:
        if i in consonants:
            consonants_count+=1
    print(f'vowels : {vowels_count}')      
    print(f"consonants : {consonants_count}")      
counter()
while 1:
    p = input("start? (y/n): ")     
    if p.lower() == "y":
        counter()
        input()
    else:
        break    
