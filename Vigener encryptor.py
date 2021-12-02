vigener_square = []
count = 0
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
beta = []

for a in alpha:
    beta.append(a.upper())
for i in range(0,26):
    register = []
    for j in range(0,26):
        index = (j+count)%26
        register.append(alpha[index])
    count+=1
    vigener_square.append(register)


key = []
strkey = input('enter a key ').lower()
for i in strkey:
    if i in alpha:
        key.append(alpha.index(i))

plainstr = input('Enter Plaintext ').lower()
plainint = []
for i in plainstr:
    try:
        plainint.append(alpha.index(i))
    except:
        plainint.append(i)

cyphertext = ''
count = 0
for i in plainint:
    keyer = key[count%len(key)]
    try:
        cyphertext += vigener_square[i][keyer]
        count+=1
    except:
        cyphertext += i
    
print(cyphertext)

