import random
c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ1234567890"
i=0
while i<5:
    a=''.join(random.choice(c) for u in range(5))
    i+=1
print(a)




    
