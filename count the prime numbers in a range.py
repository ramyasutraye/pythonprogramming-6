x = int(raw_input( ))
y = int(raw_input( ))
c=0
for n in range(x,y+1 ):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           c=c+1
print(c)  
