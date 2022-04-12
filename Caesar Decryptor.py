#from English import alpha, beta
#this was slower ebcause it ran the code to generate a wordlist using nltk.

alpha = 'abcdefghijklmnopqrstuvwxyz'
beta = alpha.upper()

key = int(input('key        > '))
ciphertext = input('ciphertext  > ')
plaintext = ''
for i in ciphertext:
    if i in alpha:
        plaintext += alpha[(alpha.index(i)-key)%26]
    elif i in beta:
        plaintext += beta[(beta.index(i)-key)%26]
    else:
        plaintext += i
print(f'plaintext > {plaintext}')
