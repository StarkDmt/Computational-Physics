import math
import cmath

b=10**(-20)
c=4.0


def machine_eps():
    x=1.0
    while((1+x)!=1):
        x=x/2
    return x
    
#Функция определения порядка числа 

def power(a):
    x=1
    while not ((a<10)and(a>=1)):
        if(a<1):
            x=x-1
            a=a*10
        else:
            x=x+1
            a=a/10
    return x

#Функция произведения (для подсчета ряда)    
def prod(a,k):
    i=1
    b=a
    while(i<k):
        b=b*(a-1)
        i=i+1
    return b

#Разложение корня из дискриминанта в ряд
def taylor(c,b):
    summ=-2*c/(b*b)
    lastterm=summ
    ex=0
    k=2
    while(ex==0):
        lastterm=summ
        newterm=(((-2.0*c)/(b*b))**k)*prod(0.5,k)/math.factorial(k)
        summ=summ+newterm
        k=k+1
        #выходим в том случае, когда разница уже не видна
        if(summ==lastterm):
            ex=1
    return summ
 


#Если порядок отношения b^2 к с меньше порядка машинного эпсилон-1, то все хорошо    
if(abs(power(abs(b))**2-power(abs(c)))<=15):
    D=b*b-4*c
    if(D>=0):
      x1=(-b+math.sqrt(D))/2
      x2=(-b-math.sqrt(D))/2
    else:
        x1=(-b+cmath.sqrt(D))/2
        x2=(-b-cmath.sqrt(D))/2
    if(x1==x2):
    	  print(x1)
    else:
        print(x1,x2)
#Если все плохо:
else:
    D=b*b-4*c
    if(D>=0):
        if(b>0):
            x1=b*taylor(c,b)/2
            x2=c/x1
        else:
            x1=-b*taylor(c,b)/2
            x2=c/x1
    #В случае, когда корни комплексные, то отдельно ничего изобретать не надо,
    #поскольку подкоренное выражение наоборот получается большим, а не маленьким
    else:
        x1=(-b+cmath.sqrt(D))/2
        x2=(-b-cmath.sqrt(D))/2
    if(x1==x2):
    	print(x1)
    else:
        print(x1,x2)

