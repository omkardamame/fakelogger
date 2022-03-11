import time

n = int(input("Enter Interval: "))
l = int(input("Enter No. of lines to Show at a time: "))
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
while n!=0:
    for x in range(l):
        print (current_time,'This is some random log.')  
    n-=1    
    time.sleep(1)