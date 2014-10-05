def oneargfunc(obj,method,data):
    if callable(getattr(obj,method)):
        func=getattr(obj,method)
        print func(data)
   
oneargfunc(list,'__len__',[3,4,5])



