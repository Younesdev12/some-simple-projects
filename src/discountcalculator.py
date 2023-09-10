import os
os.system('title Discount Calculator')
def count_discount():
    product_price = input("Enter the product's price : ")
    discount = input("Enter the discount percentage : ")
    if "." in str(product_price):
        result = float(product_price) * float(discount) / 100
        if "." in str(result):
            p = float(product_price) - float(result)
            s = float(product_price) - float(p)
            print(f'You pay : {int(p)}$')    
            print(f'You saved : {int(s)}$')             
    elif "." in str(discount):
        result = float(product_price) * float(discount) / 100
        if "." in str(result):
            p = float(product_price) - float(result)
            s = float(product_price) - float(p)
            print(f'You pay : {int(p)}$')    
            print(f'You saved : {int(s)}$')      
    else:
        result = int(product_price) * int(discount) / 100  
        if "." in str(result):
            p = float(product_price) - float(result)
            s = float(product_price) - float(p)
            print(f'You pay : {p}$')    
            print(f'You saved : {s}$')
        else:
            ints = int(product_price) - int(result)
            print(f'You pay : {ints}$')      
            print(f'You saved : {ints - int(s)}$')    
while 1:            
    count_discount()    
