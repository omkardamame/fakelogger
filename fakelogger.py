import time

n = int(input("Enter Interval: "))
l = int(input("Enter No. of lines to Show at a time: "))
while n!=0:
    for x in range(l):
        print ('Random Log')  
    n-=1    
    time.sleep(1)