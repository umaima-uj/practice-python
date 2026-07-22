def count_upto():
    for i in range(50):
     yield i
count=count_upto()    
print(next(count))
print(next(count))