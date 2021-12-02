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
        register.append(index)
    count+=1
    vigener_square.append(register)

key = []
strkey = input('enter a key ')
strkey = strkey.lower()
for i in strkey:
    if i in alpha:
        key.append(alpha.index(i))

cipherstr = input('Enter Ciphertext ').lower()
cipherint = []
for i in cipherstr:
    try:
        cipherint.append(alpha.index(i))
    except:
        if i == ' ':
            cipherint.append(i)

plaintext = ''
count = 0
for i in cipherint:
    keyer = key[count%len(key)]
    try:
        '''
        plaintext += alpha[vigener_square[keyer].index(i)]
        count+=1
        '''
        plaintext += alpha[(i-keyer)%26]
        count += 1
    except:
        plaintext += i
print(plaintext)
