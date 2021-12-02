#experimental caesar breaker
#this does not include a warning
from English import alpha, cleanse
ciphertext = cleanse(input('ciphertext  > ').lower().replace(" ",""))
best = [-1, -1, '']
stdfreq = {1:8.2, 2:1.5, 3:2.8, 4:4.3, 5:13, 6:2.2, 7:2, 8:6.1, 9:7, 10:0.15, 11:0.77, 12:4, 13:2.4, 14:6.7, 15: 7.5, 16: 1.9, 17:0.095, 18:6, 19:6.3, 20:9.1, 21:2.8, 22:0.98, 23:2.4, 24:0.15, 25:2, 26:0.074}
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
    if best[0] == -1 or best[1] >= squared_error:
        best = [key, squared_error, plaintext]
print(best[2])

