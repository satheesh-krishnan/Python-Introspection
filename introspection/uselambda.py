def sumfunc(f,l):
    e=0
    for each in l:
       e+=f(each) 
    return e


print sumfunc(lambda x: x*x*x,[3,5,6,7,8])
