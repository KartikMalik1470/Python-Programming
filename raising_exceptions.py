def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("this is not good - kartik")
    
a = increment('lajs4')
print(a)