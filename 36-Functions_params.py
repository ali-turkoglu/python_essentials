def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b    
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islemAdi):
    if islemAdi=="toplama":
        print(f1(8,2))
    elif islemAdi=="cikarma":
        print(f2(8,2))    
    elif islemAdi=="carpma":
        print(f3(8,2))    
    elif islemAdi=="bolme":
        print(f4(8,2))   

islem(toplama,cikarma,carpma,bolme,"toplama")         
islem(toplama,cikarma,carpma,bolme,"cikarma")         
islem(toplama,cikarma,carpma,bolme,"carpma")         
islem(toplama,cikarma,carpma,bolme,"bolme")         