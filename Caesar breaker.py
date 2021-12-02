from English import *
ciphertext = input('ciphertext  > ')

best_english = 0
sub = 0
output = ''
for key in range(0, 26):
    plaintext = ''
    for i in ciphertext:
        if i in alpha:
            plaintext += alpha[(alpha.index(i)-key)%26]
        elif i in beta:
            plaintext += beta[(beta.index(i)-key)%26]
        else:
            plaintext += i
    print(plaintext, "\n")
    if  x:=is_english(plaintext) > best_english:
        best_english = x
        output = plaintext
        print(key)
        if x == 1:
            break

if output != '':
    print(f'There is a {best_english*100}% probability that the answer is: \n{output}')
    if best_english < 1.0:
        not_english(output)
else:
    print('That was not a valid Caesar Cipher.')
        
