'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
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