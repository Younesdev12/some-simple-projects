import random
import os
os.system('title Flip A Coin')
coin = ["heads", "tails"]
heads = 0
tails = 0
while 1:
    heads = 0
    tails = 0
    p = input("Enter times to flip the coin : ")
    for _ in range(int(p)):
        x = "".join(random.choices(coin))
        if 'tails' in x:
            tails+=1
        elif 'heads' in x:
            heads+=1  
    tperc = tails * 100 / int(p)
    hperc = heads * 100 / int(p)             
    print(f'Tails : {tails} ({int(tperc)}%)')        
    print(f'Heads : {heads} ({int(hperc)}%)')  
