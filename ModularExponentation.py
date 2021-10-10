
def modular(a,b,modulo):
    if b == 0:
        return 1 
    else:
        result = modular(a,b//2,modulo)
        if b&1 == 0:
            return (result*result)%modulo
        else:
            return (result*a*result)%modulo
        

            
        

a = int(input())
b = int(input())
modulo = int(input())
print(modular(a,b,modulo))
