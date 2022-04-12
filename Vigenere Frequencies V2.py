import matplotlib.pyplot as plt
from English import *

#semi-automatic vigenere decryption (user must edit key length)

key_len = int(input("Enter setting > "))

def analysis(ciphertext):
    perfreq = {}
    best = [-1, -1, '']
    for key in range(26):
        squared_error = 0
        plaintext = ''
        for i in ciphertext:
            plaintext += alpha[(alpha.index(i)-key)%26]
        freq = {}
        total = 0
        for i in range(1,27):
            freq[i] = 0
        for i in plaintext:
            if ord(i)-96 in range(1,27):
                freq[ord(i)-96] += 1
                total += 1
        for i in range(1,27):
            squared_error += ((freq[i]/total)*100-stdfreq[i])**2
        mse = squared_error
        if best[0] == -1 or best[1] >= mse:
            best = [key, mse, plaintext]
    print(best[2])
    print(best[1])
    print()

    #user view
    freq = {}
    total = 0
    for i in range(1,27):
        freq[i] = 0
    for i in best[2]:
        if ord(i)-96 in range(1,27):
            freq[ord(i)-96] += 1
            total += 1
    for i in range(1,27):
        perfreq[i] = (freq[i]/total)*100 # relative frequencies
    k1, v1 = list(perfreq.keys()), list(perfreq.values())
    plt.plot(k1,v1)#plot observed frequencies.
    k2, v2 = list(stdfreq.keys()), list(stdfreq.values())
    plt.plot(k2,v2)#compare with standard frequencies
    plt.show()
    return best[2], alpha[best[0]], best[1]

stdfreq = {1:8.2, 2:1.5, 3:2.8, 4:4.3, 5:13, 6:2.2, 7:2, 8:6.1, 9:7, 10:0.15, 11:0.77, 12:4, 13:2.4, 14:6.7, 15: 7.5, 16: 1.9, 17:0.095, 18:6, 19:6.3, 20:9.1, 21:2.8, 22:0.98, 23:2.4, 24:0.15, 25:2, 26:0.074}

string = cleanse(input("> ").lower().replace(' ',''))

best_whole = [-1, -1, '']
overall_mse = 0
strings = []
for i in range(key_len):
    strings.append('')
    for j in range(i, len(string), key_len):
        strings[i]+=string[j]
        
outstrings = []
key = ''
for i in strings:
    a,b,mse = analysis(i)
    outstrings.append(a)
    key += b
    overall_mse+=mse/key_len
    
outval = ''
seg_len = len(outstrings[0])
for i in range(len(outstrings)):
    while len(outstrings[i])<seg_len:
        outstrings[i]+=' '

for i in range(len(outstrings[0])):
    for j in range(key_len):
        outval += outstrings[j][i]

'''
outval = ''
outstrings = []
key = ''
keys = [19,5,3,18,5,20]
for index, item in enumerate(strings):
    outstrings.append(caesar(keys[index],item))
    key += alpha[keys[index]]

for i in range(len(outstrings)):
    while len(outstrings[i])<seg_len:
        outstrings[i]+=' '

for i in range(len(outstrings[0])):
    for j in range(key_len):
        outval += outstrings[j][i]

'''
print()
print(outval)
print()

while True:
    count = 0
    
    for i in range(key_len):
        newout = ''
        swap = input("> ")
        s = swap.split(' ')
        if len(s) == 2:
            for j in range(len(outstrings[i])):
                if outstrings[i][j] == s[0]:
                    newout += s[1]
                elif outstrings[i][j] == s[1]:
                    newout += s[0]
                else:
                    newout += outstrings[i][j]
            print(newout)
            print(is_english(newout))
            outstrings[i] = newout
    outval = ''
    for i in range(len(outstrings[0])):
        for j in range(key_len):
            outval += outstrings[j][i]
    print(outval)

