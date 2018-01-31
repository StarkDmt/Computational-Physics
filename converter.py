dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def to_arabic(roman):
  i=0
  res=0
  while i<len(roman):
    if i==len(roman)-1:
      res+=dict[roman[i]]
      i+=1
    else:
      if(dict[roman[i]]<dict[roman[i+1]]):
        res+=dict[roman[i+1]]-dict[roman[i]]
        i+=2
      else:
        res+=dict[roman[i]]
        i+=1
  print(res)
  
def tens (n):
  d={10:'X',9:'IX',8:'VIII',7:'VII',6:'VI',5:'V',4:'IV',3:'III',2:'II',1:'I'}
  return d[n]

def ls (n):
  res=""
  if ((n>=40) and (n<50)):
    res+='XL'
  elif ((n>=50) and (n<90)):
    res+='L'+'X'*((n-50)//10)
  elif (n>=90):
    res+='XC'
  else:
    res+='X'*(n//10)
  n=n%10
  res+=tens(n)
  return res

def ds(n):
  res=''
  if ((n>=400) and (n<500)):
    res+='CD'
  elif ((n>=500) and (n<900)):
    res+='D'+'C'*((n-500)//100)
  elif (n>=900):
    res+='CM'
  else:
    res+='C'*(n/100)
  n=n%100
  res+=ls(n)
  return res
  
def to_roman(n):
  m=n//1000
  res=""
  for x in range(m):
    res+='M'
    n-=1000
  res=res+ds(n)
  print(res)
    
  
to_arabic('XXXIX')    
to_arabic('CCXLVI')
to_arabic('MDCCLXXVI')
to_arabic('MDCCCLXXXVIII')
to_arabic('MMMCDXLIV')

to_roman(39)
to_roman(246)
to_roman(1776)
to_roman(1888)
to_roman(3444)


    
