
#string = cleanse(input("> ").lower())
#orig = string
#freq = {}
stdfreq = {1:8.2, 2:1.5, 3:2.8, 4:4.3, 5:13, 6:2.2, 7:2, 8:6.1, 9:7, 10:0.15, 11:0.77, 12:4, 13:2.4, 14:6.7, 15: 7.5, 16: 1.9, 17:0.095, 18:6, 19:6.3, 20:9.1, 21:2.8, 22:0.98, 23:2.4, 24:0.15, 25:2, 26:0.074}
#perfreq = {}
print("program active")
import json
import matplotlib.pyplot as plt
from English import *
with open("digrams.json", mode = 'r') as file:
    digrams = json.loads(file.read())
print("imports done")

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
alphanum = 'abcdefghijklmnopqrstuvwxyz1234567890'
inp = '6WINFVHJU2ONTIA2P256WLHP5845RDQD89HP5CFNRFYVCOVP6WVXONUPOF89HPPVOVVJVP3PEYAWPWY8RDNPE5CPAVFN75W6AWBYJR2U4B56VZVOYP6WINFVRZEYP00PWLHP5845RDQD89EYOAAU96UY2BHRPW0EN3RFYVCOC2ZVZHWPHYITHP6AOGQD2UOSCOAWNFAWIEBDMPKDV5F98OHPJR8448HYWVBYRHFROVE5TNAVJOYOHZNFNHVP98WVW6YBAR0EBVDR54O8CWUYQDHPOVFVTMZH89BYVJP0UV0PYBARRJN6NF2BWLHB5VAWOVTNPMC5BWVPIHFNNFAWHZAMPMYDVONFAW0PLEN3VF5CACMPN3H3GO560EBVDR56AW2EVO2B75HPFV75MPYPA6AWVAOEEYN3RZHZ5C89ONPMPWCRPMZRC24BPC56HZTNYURBZHAM5CACYPC5DR2UYXRANOVD5UEY0BC5VO2THFAMACTETNPWUAIETMW62H56IWIADRHPJRDYFNOH89EYAW2TYNARBXVP0EBVDRAUFNRAWPDEMBTMPWDRCKQDDROCHNFNE0YUO8VJ8456AWPWPMFVIE45IELCDRACHPPW8995VOCWNFVAHWYOPMWRAUN6R895WK2CRDQDRFUYPURYZHHFAMACN6RJLEVON3RJE5CTYBZHPDB2BYRH86JH8OCHFNXHWEHWBYCORFOJSA8O0EYBARYPRFHYBY6AJADRBAPWUPOANZBYRBRDHNOV58A396QIVOPWOVIEAFKVV5VDOCHNFNEYSOEYAWOVDEO82BVAVPOFBVPMTN89YOHZVOP0JRACHPOCLE8OWPVD58PZVPW6NADRIKPZVP0EBVDR56CK6AWNRPVOIVYCUPW6W62PE50PU5YPVPVIEWVFYPCKHPOVHPOUYAQOACYDHPDPDLDPCKTN56ZHYPVA6AIAHPOVHZFRNP456AC06759TMMTVF89HPAVAUUPBVRA2PXYFVHPPWUAVOCPIE2CQDENOD0PTBPUPYVPCUE246VOBWPYVPCARCU5NZAVAYNPE5ENOD0PTBPURPVF56H2U2EDRBVAN3VF5C95PCMPCTWLHPOU98VOFP6WAYACHPAMAVXYVAHZNPWHAY98V2HPPCEDPGAR5898YVYAQONPOEFVYBQDCAUY4POVDRDKAW6AP0ZRDRBXVPNEHZP3AY89DR98V2PWY8A6IVFRHZVPUPMPIQ64RBDVPUYAQO6AW6BD2PYDQDZVYPVFAUVPVO6AWNVPAN5U6ANPE5HPKCVOPWFVYBSAMTAVU5BYJRRAEDUYCAHWHPPWEYSOEYAWOVNZOVAUE2AV98VIACITIEAEAVYBARYPKUOVH4AYOVITVZTHMP45OFWERJARNOHPOVHP6A98VIPUVPRO5UKIRDUFBWVP48UAO8PZNPULAIZV84OV6AWYYPBV6ACKRFUYPUZO8OIKAI6ABWVPRN8O75BWYOPMFVH3RNBYPHNPWPC2UAONPUVP98HYWVPWPVOCOF89HPPWYH6WBYY8ANBYPHRBFAAU96UY2BHROHERYWDRCXNZBYP4AYOVCPR8AWHPOCOP84FVJORAHTOUARBWVPYOIN563VYDHPHPJR48UAVIE2FV6NONRDQDEYNOTY2BHRYPVFAUNPULOWIEC5YATMWT5895RAV2EYFEP0V5YPEYVOVA2CFVHPACE0KDPUNPUBEY0BCPIAVAITHPFRAURPVFOD2CHZVPIEHWO82PASPWY8AF6AWN56BHRBPZVPTR6WEDU5N3HZA2EYV2EDRBVANFAWAQAYMPWXOCVZHWRBQAPDMPHPJR48UAV2ZVYH5CODAPYWCAVAE5SAO8LURPVFUAYAQOYPVFOE59P22PYDQDHPAMKUE04B5898YV98WVCAOFUAYDBDMPUKHYEYOYSAMTAVU5ITHZ56BHPH67DRBKFRBYY8AFDRRFUYPURNVPVOUADEHDFVZHNP45BYZVDRIKYVPDB2BYRH898O5UFNWBBO2P0EYBU5IERA2CDEAWRFUYP0HZ8O3VDR8OCAHYPRPM48YVA6YBARHZAY56HPOVHP5CPWRAYBC5DEAN56A398NIYPUPBDBHVP0UNPHN56VOIADRDQ8ORPNDUAONAC8YQDBYHPOV56VOHPFRAUBYRBRAYVIKE5OAC5HWTNAYEY0BVF58YVDE46TY2BHRDRUPV2RFAZON96VOTNB2AU56VOCAWYDEUPBWPYVPOH5EAVYBAR89IESA2BBUHPOUYATMBWYVRDYBAFUP6WDRYP6N5648ANBYPHNPHN5648HWVPRNEY0BCTB2W6YAH2WYHWVPYOAYRD0ECK48JRARACITRCP2AVU56AWXVOAC89IEYVVFHPOVOCNFOYQFDRTNPWUAIAYDHPEYYH5E562BQDHP5CEDRBVANFAWHPOCNY8OOGQDRJUB6ACPWYA3OJUVBH6AJNE2PUC2FVC248N3RJTBPUEIARRCVD58YVIKE5OAC5HWRFOJLEAVWYQDW6QDOVUAON56BD1BYCBHR8OS59ZVDRBX89EDPUVPYHVHNPWLYBC5NZVPRDWB85FAPYVZBYZVCTHN5CZVWH5EOVRYPMBWPYVPUPLEWPYBARYPVOE5P0EYOF5UVOHNVPVOUADEAOFVNP45CAHZDRRN5CZVHNVPVOUADEADRAWBFRAYBYRPVHOYQF89WYVJEROVRN5U6ARAYBHPFNCPAVHPKCVOPWFVZB8RYPIHDRBXRBHFO8CFBUYPBYVJARBMZVY8APOV56WLHPPV56HY89CPEWHRTNOVAU56VO6NACITHPPUVTAWOV89HP59P03HHPPWINCR58YV0EBVDRFVUAONPMGOPUVPVZANRPVFVPPWVOMPFNFVHPPU8OVOHW89C5BHN6UPHYNPUBONE5RJZHN6WIAYHWPOEYBQO8GENFAWARYPHPPC0PCANZRBBVINCR58YVCKVANOYPOFEYHOAYOVJRDRWYVOBUCTYBN2VORJHZYTMP6AWU64PDMP89BV6AXYQDHPDRJQ98VOE5HIVHUAP0RFHZ6ABNVCTBACITHPFRAURPCTB2WLHP57RAT0ACCKAVPD2BQDEYV2EDRBVAF9O8LUVPPMCAOF89IQAM570EHP5CPWYUVFVU2BW6AWRT46YBPWPOEYBQYPDPDLDPCK6AB0ERPMEDPUNPXPRAT0ACCKIAFVRAHTPMARBXEYHJVHJRAVYHZVUPBWA2EYQIAVOVPWY8HDRHRPVFTNAYAVHT598O56NZFVWPAWVPVODR0EN3RFYVCOBYVF5CV38OPUNPA6ALOH84OYPWPU86GERAT0ACCKHPPWHPOV56VOPYVPOFMPN3VJPMPCNOUPWNRPNPE5YHAICAHWVP46HPUAON58RDHF5678PZVPRBAWVCPWVP0EYBUY6ANZRPVFYAQONPJNVUNPRDSAMTAVU5AR2UWVBMKC58QIAM5EOVFVWPAW2UVTHJ6AWX58QIPCA2P2AUPVENFVYBBDBCVUPHP256OAOSE2DRWY6DPDEYWLHP54RZBVP2KIR8E3PWVP0EYBDE3HHVIWCKVANOBD2T6ABWVPVOON5C6AR8HPOVIH6ABVFV89MPONRDQDDRTNYURPYV48UAOFONFVYBBDBD0PUPHWN6BYDRBXVPYPVURPOJAWDOYPHP6NHP5CDRYP2B95VOMPFNDRIKYVOSFYAVIAV26AZPEDTMYBFVOSE2YHDRBYRNNPSOYPRFVHOV48DRHNFVAMPUVP48UAO8ASAUPM5UYHYUP02T48UAVOBW5UPAP2KICOHZFRRBVAP0YXPHAR0EOYVAOFIFYVVAZR6ABWAYONHWVP0EN6ZOO8LUVPO8GERFYV8ODKRDNFYBARN6F9EYAWACYP4BOWHPFVE0OVP2OCAFEICOHRYPAV2BBQUPA6AWYPN6OA6AWN56VOHPPMYXPHRPZV57AM54OVNZRPVFIFTYYBHZ87AM54HPPME04BBY6ABWYVRDQDFNHPKCAVOVPW8OHJKCDRYPHVOA48UAOYQDHPAVKUZHWPCKDREYNI5EPM84C5HWC2ZVYBN3VZ56VO2CAWOVYPR8WEBDBHVP0EBVDRFVONFCZVYPVA46HY896AAV8O2EZVAVUPHOOYVFYDHPEYHREYNY8O76BDBHVPDEMBTMPWY8AFDRHPAU8O0BYATMBNENAV8YLEEDHTVHRAYDYBHZC2598OC5YPOJRDFP6AJNWPAWFNYW5VH0GOPUVP0EBVDRFVUAON5C8OWP0PAWHPPUC2AUB2MBE2598OR8WERJHPFN98V2PUFRUPABAYSAO82UEYN2O8MPNZBYPHNPYBV0DRIWEYCVHZ98VOE5HI56MPHYYPHPFRAURP2CBQWLWP75R8YV4BEDOCHWVP2BBQHPEYVFYDHPEYWHAUC5LCOVRFYV2CN3RJARYDBD0BCO6AJNAYB2BC6ARYADRAU5HWNZRPVF2BE5V3OWCPNFE5WTR8YVU5FNPMFVNZ8O798OP02BZH48UAHYVP0EBVDRPVFNCPAVWVPDMPYPUPBDMTHZVPEZHVVO89EYO8QI6AJRPWY8RDAFUP6WUACVHZIEHWDRV5YPCTB2WYZP8OEYOFPME5RFVAW6WOWPYBC5DYJRRTEYP0MPE5OR98HYWVOCHWNPUBVYUYP0YAQO'
text = inp.lower()
freq = {}
for i in alphanum:
    for j in alphanum:
        freq[i+j] = 0
for i in range(0,len(text),2):
    freq[text[i:i+2]]+=1

ret = decodify(freq, digrams)
def getout(text,ret):
    output = ''
    for i in range(0,len(text),2):
        if text[i:i+2] in ret.keys():
            output += ret[text[i:i+2]]
        else:
            output += inp[i:i+2]
    return output

print(outval:=getout(text,ret))




        
def sortify(d):
    '''takes dict, sorts by key (selection sort), returns sorted dict'''
    keys = list(d.keys())
    values = list(d.values())
    new_keys = []
    new_values = []
    if sorted(keys)==keys:
        return keys, values
    else:
        for i in range(len(keys)):
            index = keys.index(min(keys))
            new_keys.append(keys.pop(index))
            new_values.append(values.pop(index))
        return new_keys, new_values

#print(outval)#populates and returns output


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
with open("trigrams.json", mode = 'r') as file:
    trigrams = json.loads(file.read())

#print(ret)
overall = 0
total = 0
for i in range(len(outval)-1):
    total += digrams[outval[i:i+2]]
overall+=total
print(f"digram score (higher is better):   {total}")

total = 0
for i in range(len(outval)-2):
    if (test:=outval[i:i+3]) in trigrams:
        total += trigrams[test]
overall+=total*10
print(f"trigram score (higher is better):  {total*10}")

overall+=10/meansquare(outval)-1
print(f"frequency score (higher is better): {50/meansquare(outval)-1}")

print(f"normalised score: {overall}")

###create iterable list

print(overall)

swaps = {}

for i in range(26):
    for j in range(i,26):
        swaps[alpha[i]+alpha[j]]=alpha[j]+alpha[i]

best = outval
lastscore = -1
score = overall
while score > lastscore:
    lastscore = score
    scores = []
    texts = []
    rets = []
    for k in swaps.keys():
        newout = ''
        s = [k, swaps[k]]
        if len(s) == 2:
            if s[0] in ret.values() and s[1] in ret.values():
                temp = ret.copy()
                
                newout = getout(text,ret)
                #print(newout)
                outval = newout
                #elif 
                #print("value not in list")
                #print(ret)
                overall = 0
                total = 0
                for i in range(len(outval)-1):
                    total += digrams[outval[i:i+2]]
                overall+=total
                #print(f"digram score (higher is better):   {total}")
                
                total = 0
                for i in range(len(outval)-2):
                    if (test:=outval[i:i+3]) in trigrams:
                        total += trigrams[test]
                overall+=total*10
                #print(f"trigram score (higher is better):  {total*10}")

                overall+=10/meansquare(outval)-1
                #print(f"frequency score (higher is better): {50/meansquare(outval)-1}")

                scores.append(overall)
                texts.append(outval)
                rets.append(ret)
                ret[list(ret.keys())[list(temp.values()).index(s[0])]]=s[1]
                ret[list(ret.keys())[list(temp.values()).index(s[1])]]=s[0]
        elif s == ["ret"]:
            print(ret)
        if k[1] == 'z':
            print(f"done {alpha.index(k[0])+1} of 26")
    if max(scores)>lastscore:
        score = max(scores)
        ret = rets[scores.index(score)]
        best = texts[scores.index(score)]
        print(score)
    
    
print('best answer found!')
print(f"it scores: {score}")
print('it reads:')
print(best)
print("achieved using")
print(ret)
    
