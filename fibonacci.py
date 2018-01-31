lst = [1,1]
while (lst[-1] + lst[-2])<(4*(10**6)):
  lst.append(lst[-1] + lst[-2])
a=0.0
b=0.0
for x in lst:
  if(x % 2 == 0):
    a=a + x*x
    b=b + x*x*x
print(b/a)
