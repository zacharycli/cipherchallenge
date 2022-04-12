a='abcdefghiklmnopqrstuvwxyz'
b=input().split(' ')
c=''
def p(s):
  print(s,end='')
for i in b:
 try:
  p(a[(int(i[0])-1)%5*5+(int(i[1])-1)%5])
 except:
  p(i)
  if c==i:
   p(' ')
 c=i
