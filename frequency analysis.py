import matplotlib.pyplot as plt
from English import *
string = input("> ").lower()

freq = {}
stdfreq = {1:8.2, 2:1.5, 3:2.8, 4:4.3, 5:13, 6:2.2, 7:2, 8:6.1, 9:7, 10:0.15, 11:0.77, 12:4, 13:2.4, 14:6.7, 15: 7.5, 16: 1.9, 17:0.095, 18:6, 19:6.3, 20:9.1, 21:2.8, 22:0.98, 23:2.4, 24:0.15, 25:2, 26:0.074}
perfreq = {}
           
def sortify(d):
    '''takes dict, sorts by key (selection sort), returns sorted dict'''
    keys = list(d.keys())
    values = list(d.values())
    new_keys = []
    new_values = []
    if sorted(keys):
        return keys, values
    else:
        for i in range(len(keys)):
            index = keys.index(min(keys))
            new_keys.append(keys.pop(index))
            new_values.append(values.pop(index))
        return new_keys, new_values
    
    
for i in range(1,27):
    freq[i] = 0
total = 0
for i in string:
    if ord(i)-96 in range(1,27):
        freq[ord(i)-96] += 1
        total += 1
#freq stores total number of each char used
#total stores total number of all valid chars used.
for i in range(1,27):
    perfreq[i] = (freq[i]/total)*100 # relative frequencies

k1, v1 = list(perfreq.keys()), list(perfreq.values())
plt.plot(k1,v1)#plot observed frequencies.

k2, v2 = list(stdfreq.keys()), list(stdfreq.values())
plt.plot(k2,v2)#compare with standard frequencies

plt.show()
#now that that's out of the way, the fun can begin...
def decodify(d, p):
    '''takes two dictionaries, pairs up their max values, returns a conversion dictionary which carries the original paired with the decoded char'''
    dkeys = list(d.keys())
    dvalues = list(d.values())
    pkeys = list(p.keys())
    pvalues = list(p.values())
    ret = {}
    for i in range(26):
        i = pvalues.index(max(pvalues))
        j = dvalues.index(max(dvalues))
        
        dkeys.pop(0)
        
        if sum(dvalues) == 0:           
            break
        pvalues[i] = 0
        dvalues[j] = 0
        if j+1 in ret:
            print()
            print("damn")
            print("ret looks like ", ret)
            print("wants to write to index ", j+1)
            
            print("the value ", i+1)
            print("overwriting ", ret[j+1])
            print("origp", list(p.values()))
            print("p", pvalues)
            print("origd", list(d.values()))
            print("d", dvalues)
            print()
            
        ret[j+1] = i+1
    return ret

ret = decodify(perfreq, stdfreq)

outval = ''
for i in string:
    if ord(i)-96 in list(freq.keys()):
        outval += chr(ret[ord(i)-96]+96)
    else:
        outval += i
print(outval)#populates and returns output

englishness = is_english(outval)
print(englishness)


#analyse the output

freq = {}
perfreq = {}
for i in range(1,27):
    freq[i] = 0
total = 0
for i in outval:
    if ord(i)-96 in range(1,27):
        freq[ord(i)-96] += 1
        total += 1
for i in range(1,27):
    perfreq[i] = (freq[i]/total)*100
k3, v3 = sortify(perfreq)
plt.plot(k3,v3)
plt.plot(k2,v2)
plt.show()
plt.plot(k1,v1)
plt.plot(k2,v2)
plt.plot(k3,v3)
plt.show()

while True:
    count = 0
    newout = ''
    swap = input("> ")
    s = swap.split(' ')
    if len(s) == 2:
        for i in range(len(outval)):
            if outval[i] == s[0]:
                newout += s[1]
            elif outval[i] == s[1]:
                newout += s[0]
            else:
                newout += outval[i]
        print(newout)
        print(is_english(newout))
        outval = newout
