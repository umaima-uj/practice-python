import time
animal=["dog", "cat","lion","deer","leopard"]
init=time.time()
for i in animal:
    print(i)
    time.sleep(3)
t1=time.time()- init    
print(t1)
t=time.localtime()
actual_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(actual_time)