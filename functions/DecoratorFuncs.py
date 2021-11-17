

def PermissionCheck(asd):
    def wrapper(cls,request):
        print(cls)
        print(request)
        asd(cls,request)
    return wrapper