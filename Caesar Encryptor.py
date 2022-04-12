#from English import alpha, beta
#this was slower because it ran the code to generate a wordlist using nltk.

alpha = 'abcdefghijklmnopqrstuvwxyz'
beta = alpha.upper()

key = int(input('key        > '))
plaintext = input('plaintext  > ')
ciphertext = ''
for i in plaintext:
    if i in alpha:
        ciphertext += alpha[(alpha.index(i)+key)%26]
    elif i in beta:
        ciphertext += beta[(beta.index(i)+key)%26]
    else:
        ciphertext += i
print(f'ciphertext > {ciphertext}')


