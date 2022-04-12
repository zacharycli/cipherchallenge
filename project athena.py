# breaks monoalphabetic ciphers using monograms, digrams and trigrams
# matches most common bigrams using decodify
# uses a vote based system
# will break any monoalphabetic cipher instantly
# It's better than any other historical method
# It will be tested to be effective when the box is checked: [ ]
print("program active")
import json
from statistics import mode
from English import alpha, cleanse
with open("trigrams.json", mode = 'r') as file:
    trigrams = json.loads(file.read())
with open("digrams.json", mode = 'r') as file:
    digrams = json.loads(file.read())
print("imports done")
def sortify(d):
    '''takes dict, sorts by key (selection sort), returns sorted dict'''
    keys = list(d.keys())
    values = list(d.values())
    new_keys = []
    new_values = []
    if sorted(keys) == keys:
        return keys, values
    else:
        for i in range(len(keys)):
            index = keys.index(min(keys))
            new_keys.append(keys.pop(index))
            new_values.append(values.pop(index))
        return new_keys, new_values

def decodify(d, p):
    '''takes two dictionaries, pairs up their max values, returns a conversion dictionary which carries the original paired with the decoded char'''
    dkeys = list(d.keys())
    dvalues = list(d.values())
    pkeys = list(p.keys())
    pvalues = list(p.values())
    ret = {}
    #print(dkeys, pkeys)
    #print()
    length = len(dkeys)
    for k in range(length):
        i = pvalues.index(max(pvalues))
        j = dvalues.index(max(dvalues))
        if 0 in [max(pvalues),max(dvalues)]:
            break
        #dkeys.pop(0)
        
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
        #print(j+1, dkeys[j])
        ret[dkeys[j]] = pkeys[i]
    return ret

votes = [3,1,0]

text = cleanse('To Sherlock Holmes she is always the woman I have seldom heard him mention her under any other name In his eyes she eclipses and predominates the whole of her sex It was not that he felt any emotion akin to love for Irene Adler All emotions and that one particularly were abhorrent to his cold precise but admirably balanced mind He was I take it the most perfect reasoning and observing machine that the world has seen but as a lover he would have placed himself in a false position He never spoke of the softer passions save with a gibe and a sneer They were admirable things for the observer—excellent for drawing the veil from men’s motives and actions But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results Grit in a sensitive instrument or a crack in one of his own highpower lenses would not be more disturbing than a strong emotion in a nature such as his And yet there was but one woman to him and that woman was the late Irene Adler of dubious and questionable memory I had seen little of Holmes lately My marriage had drifted us away from each other My own complete happiness and the homecentred interests which rise up around the man who first finds himself master of his own establishment were sufficient to absorb all my attention while Holmes who loathed every form of society with his whole Bohemian soul remained in our lodgings in Baker Street buried among his old books and alternating from week to week between cocaine and ambition the drowsiness of the drug and the fierce energy of his own keen nature He was still as ever deeply attracted by the study of crime and occupied his immense faculties and extraordinary powers of observation in following out those clues and clearing up those mysteries which had been abandoned as hopeless by the official police From time to time I heard some vague account of his doings: of his summons to Odessa in the case of the Trepoff murder of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee and finally of the mission which he had accomplished so delicately and successfully for the reigning family of Holland Beyond these signs of his activity however which I merely shared with all the readers of the daily press I knew little of my former friend and companion One night—it was on the twentieth of March 1888—I was returning from a journey to a patient (for I had now returned to civil practice) when my way led me through Baker Street As I passed the wellremembered door which must always be associated in my mind with my wooing and with the dark incidents of the Study in Scarlet I was seized with a keen desire to see Holmes again and to know how he was employing his extraordinary powers His rooms were brilliantly lit and even as I looked up I saw his tall spare figure pass twice in a dark silhouette against the blind He was pacing the room swiftly eagerly with his head sunk upon his chest and his hands clasped behind him To me who knew his every mood and habit his attitude and manner told their own story He was at work again He had risen out of his drugcreated dreams and was hot upon the scent of some new problem I rang the bell and was shown up to the chamber which had formerly been in part my own'.lower().replace(' ',''))
stdfreq = {1:8.2, 2:1.5, 3:2.8, 4:4.3, 5:13, 6:2.2, 7:2, 8:6.1, 9:7, 10:0.15, 11:0.77, 12:4, 13:2.4, 14:6.7, 15: 7.5, 16: 1.9, 17:0.095, 18:6, 19:6.3, 20:9.1, 21:2.8, 22:0.98, 23:2.4, 24:0.15, 25:2, 26:0.074}
swaps = {}
for i in range(1, 27):
    swaps[i]=[]
freq = {}
perfreq = {}
for i in range(1,27):
    freq[i] = 0
total = 0
for i in text:
    freq[ord(i)-96] += 1
    total += 1
for i in range(1,27):
    perfreq[i] = (freq[i]/total)*100
temp = decodify(stdfreq,perfreq)
for k in range(votes[0]):
    for i in temp.keys():
        swaps[i].append(temp[i])
#print(swaps)
#{1: [20], 2: [7], 3: [13], 4: [4], 5: [5], 6: [21], 7: [25], 8: [8], 9: [15], 10: [24], 11: [22], 12: [12], 13: [3], 14: [14], 15: [9], 16: [16], 17: [17], 18: [18], 19: [19], 20: [1], 21: [23], 22: [11], 23: [6], 24: [10], 25: [2], 26: [26]}
freq = {}
perfreq = {}
for i in digrams.keys():
    freq[i] = 0
total = 0
for i in range(len(text)-1):
    freq[text[i:i+2]] += 1
    total += 1
for i in digrams.keys():
    perfreq[i] = (freq[i]/total)*100
temp = decodify(digrams,perfreq)
#print(temp)
for k in range(votes[1]):
    for i in temp.keys():
        swaps[ord(i[0])-96].append(ord(temp[i][0])-96)
        swaps[ord(i[1])-96].append(ord(temp[i][1])-96)
#print(swaps)
#input()
freq = {}
perfreq = {}
for i in trigrams.keys():
    freq[i] = 0
total = 0
for i in range(len(text)-2):
    freq[text[i:i+3]] += 1
    total += 1
for i in trigrams.keys():
    perfreq[i] = (freq[i]/total)*100
temp = decodify(trigrams,perfreq)
#print(temp)
for k in range(votes[2]):      
    for i in temp.keys():
        for j in range(int(50/stdfreq[ord(temp[i][0])-96])):
            swaps[ord(i[0])-96].append(ord(temp[i][0])-96)
        for j in range(int(50/stdfreq[ord(temp[i][1])-96])):
            swaps[ord(i[1])-96].append(ord(temp[i][1])-96)
        for j in range(int(50/stdfreq[ord(temp[i][2])-96])):
            swaps[ord(i[2])-96].append(ord(temp[i][2])-96)
print(swaps)    
for i in swaps.keys():
    if swaps[i] != []:
        swaps[i] = mode(swaps[i])
print(swaps)
outval = ''
for i in text:
    if ord(i)-96 in range(1,27):
        outval += chr(swaps[ord(i)-96]+96)
print(outval)



def meansquare(string):
    perfreq = {}
    freq = {}
    total = 0
    squared_error = 0
    for i in range(1,27):
        freq[i] = 0
    for i in string:
        if ord(i)-96 in range(1,27):
            freq[ord(i)-96] += 1
            total += 1
    for i in range(1,27):
        squared_error += ((freq[i]/total)*100-stdfreq[i])**2
    return squared_error

total = 0
for i in range(len(outval)-1):
    total += digrams[outval[i:i+2]]
print(f"digram score (higher is better):   {total}")

total = 0
for i in range(len(outval)-2):
    if (test:=outval[i:i+3]) in trigrams:
        total += trigrams[test]
print(f"trigram score (higher is better):  {total}")

print(f"frequency score (lower is better): {meansquare(outval)}")
