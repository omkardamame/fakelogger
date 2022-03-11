import time

n = int(input("Enter Interval: "))
l = int(input("Enter No. of lines to Show at a time: "))
while n!=0:
    for x in range(l):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print ("This is some random text and today's time is ",current_time)  
    n-=1    
    time.sleep(1)