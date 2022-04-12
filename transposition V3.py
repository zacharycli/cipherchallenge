print("This program requires the ciphertext hardcoded. Standard input is not available")
print("Processing is likely to take up to 5 minutes. Please be patient.")

from itertools import permutations
from English import cleanse
import re
def col_wise(a, n):
    word = ''
    for i in range(0,len(a)//n):
        for j in range(n):
            word += f"{a[j*len(a)//n+i]}"
    return word


def listify(a, n):
    words = []
    for i in range(0, len(a),n):
        words.append(a[i:i+n])
    return words

def create(words):
    shuffledwords = []
    for i in words:
        shuffledwords.append([''.join(i) for i in permutations(i)])
    output = []
    for i in range(len(shuffledwords[0])):
        output.append('')
    for i in range(len(shuffledwords[0])):
        for j in range(len(shuffledwords)):
            output[i] += shuffledwords[j][i]
    return output

import json

print("\nImports finished, commencing file load.")

with open("digrams.json", mode = 'r') as file:
    digrams = json.loads(file.read())
print("File load complete. Stand by for possible answers.\n")

text = "nspaedtuppnotnyseoesrsthsotrsieteathomneyoasavhensmmnoseuteathuphaephelpanatndoosiislecetonectchatonurayiresryerounspaedoaanrilyrsthsotrsieteaanldarodicalunndroecyoasavolotrtemdiacthrenketayeyavatewatmaeemeafyayestthurswwadipoontyeihaleadtodffaitewudheelpochenveroshinrnllddicetthhaedairteaonepricilyenveliusewalrsdgglathaadtibetahelmneewatitowtidoerewatlykeecngomormeecslboesroshinesatyheralctthedctmeoumoatofltanecoaitomeanotindrmtiwnolirdhesitadtlwhrtowomoroubeinayohttgedbulanebbeerrrbloworkaadndhimaaichjuesgitwinthursbnedweaanatrrrvveamheroshinarnettemdtyiaindinraetinwilaneigtlllepswesatndtiedmatrmapiinorthndeagaerddewoftefatihsarusfogapscasietyoicnttmrtbloworuslikeerecliletsenrtefidontynbpustymnedpifteonavyoieilstroenveouyodionreptinuendseldcoonwhsilahasodrodfrerndhamapegsyadbwilaneanucanathadtllalofheutshtiadeafaiterriurorthwikestemdbsobuhechdciniobuheroshinesrarefihoernluasechchmilelyweouhescakngourathhathytdancordothapruapraadesrtouofretwthhaiteiistrreycluosaiprngeathtoarseshttmiegedthndhiercemacaetgoaglyocntdshefuftsuertadshessmpwecotosaislegoaglyocnthongessnppdewhofecngomgadhmetsrsthytelerdlnssaorthowtoegofitisnysaelnithdhdeogvesoelasdancisltedenetssicjehainsfatreriwninamhesyitipsaeainelnindoomonleiithesemetbnmwhoyntdancrecheemidoetotoungarheerrefiheevulreislethrderndedenilprtoweonurttdeicsstethndanucanathacohaarfttoelscoracmahrtoenveouplharpsahaacrylwmetrutiflivegethhathreelscnthektulobsiiktahewahillbuistcopotswharelooushrerayoicntrcstioopretaheimstcttafatiedslimonehisemolhinontheeldipondupwiuteathndghnsonooevonehwhbrarodicalundwiadyinybcoonsdsahacefoatthwiccsweddfttfeytvetahefapaesrgdoththurwahiscftedrhnosietangeclalunoungaristcvimabedaainfsogattnianrbriyaouanerofcaedthorigafntisspanebcetwofactheiarhongagcaithematellmiokndooperefiesnawhbuheypnsdeweecitysannidewhofewatmssameivwirytewhubefmethurwahiniotghomagdmdyssofleilllnwhonghidancoungltoseomidoetthowpligirsoelaselpossuthidoeemetddianhtilprtoweacitesnaehluinyfeionoopeinyoicntimheerhidtcredrtistronotinioasefidontyeastulnegtmrmiroenwemattcadtatyoicriitstrginstssdimbtiwaasmoenveitsaesthhathomndttenbedtevesdrelquouseeenahemwislaesertwinhhsthonuhinoormtetonthhaesertheiaronwhttasioleldbeteadsaanebngsoasdtsuclaluninseniyohunooderadidaresersslodtsetadshedwabtoenveeamailalsmthytdaaitaassienpesensinourheswaevonehislaeswateheimanebtsidchdasnlotehefasasirorawaurveoracmpeotowereiveroreamaasngthhawiewhtmuinadndhitwdothanghabesaletthomdewhofewatthwiexstnketlisprecelodriecinareckftntoledolwaecliocntkivempdbsoasioleldbeteyoieketoloetchethahinoeseeuwuanafoeyosotinameadentheghmyisrsenbecohesigtwtbrdsryonottslaomotnyabhatmtitadshesekeemenveouerlerianutulerlaheerhidtcuedistrssitinimomotlaheerhidtgrttgteisaonhomyhtmuealoepiahaimulrettenthnecetothrderndedhmtgoulminamwhblllrfsmouonepveoiotoodmhaesrsthupesdieaceakunadhaareserrhoracthntbyathaeathosriumthndparmsoasroshinedhinotibontheryevhonghendermeneedthntsterteeabenaussediisspnolelirtushwsaterkanwollugewatveouthdhlysscowhshparmsoasraofgeouutanrlsahaurinloersmtsenduerliitekmeretpnmefmeeashreegetthineuelerlelsmyhiriyoitreovuiocoractheiarhotsidrsthihttaworratoefaletannidewhofyellnwhetissuteatbowihrothomndtlngnhalchatffsuenndrkanwoouapruapraretfiatidentisfmttaworratwedttfetiveamantumyurtoghotsetaysanfrtohandoocrtyhongadsatofeosstescoedematheerinroecyoasavonngomgustntismokndwswhtndntnbugttaworrathndthhaeserdsheutmeeceptidhgesefihoisleghopsstehesuthhinososiblesuhbuhewhatuindheroenicrecohongdanciscknhissiilprtoweveaypooirdsofrowabhaedemataybytureivsofrdhyseoarupgoedeneebanheheoesldeyftinlofsefanrsthrnoasheoobfoibndheroendtumrwgiraofgeeerrretaheernoomrefothhalmreshedeamenosietinadtlhoaswahiutnoedeneeeelyseteusoninamheounhhoieatnnouthrhthominoualgaermeneinioaseyfhtotwnirelfdeaienedeyftghinonimisucouyomyhawainlaedownthewahillokartiulghtlrirrwahiertaulfleoobaviteiwhofriohehverohtofutdnasofwnretasanoteherousrcllnwhellugyoasstsfsiewenveusyeanatorouirvithedighaeowipekiavunoutoalwosemoatouusldrefieserthtiohehhootihowrnhacohongdnclenitwsowrnthtiigironretaassietnethrdtohandstturdinourwldwahihtetthtoplrtemrainanquabtiswbeteolotenecryesercaathaoufoifeenaheroshinednohyotouofsudiearetostyhottoserlhtngdothanunanexstvaeenahedtyiaindoopeintharstebdaaiovgotomtkedefemyttdoenitolosstbeouiesidlreckematnedyglydbontheroshinedhinoomstemlyatthntolaridyiftosstfoiflithneelninteiseiwsailllayandullmecoonehisensringianywitelerlelsesmedioutheiarhocaworsemctfoasirdewitehealwothanngdothannyarbepihayoascaeclivedoeeebavrecksaidbaretmgrttwetecohongalleguviceewlenffoaswenetiedcostyrstrialrtwahidiheroshinupnecetopoefmeouseeepritheaurwereaanllfrreurndoosipesenshiywitmateinyaoutsidlolfstanuttileyoofchylemenbesburffanrimeleskeldipowiteisspksicridanc"
text = cleanse(text.lower().replace(" ",""))

overall_scores = []
overall_texts = []

keys = []
for i in range(2,10):
    if len(text)%i==0:
        keys.append(i)
for key in keys:
    print(key)
    formatted=create(listify(text, key))

    scores = []

    for word in formatted:
        score = 0
        for digram in digrams.keys():
            for m in re.finditer(digram, word):
                score += digrams[digram]
        scores.append(score/len(word)*1000)

    #print(scores)
    print(formatted[scores.index(max(scores))])
    print()
    overall_scores.append(max(scores))
    overall_texts.append(formatted[scores.index(max(scores))])

    formatted=create(listify(col_wise(text,key), key))

    scores = []

    for word in formatted:
        score = 0
        for digram in digrams.keys():
            for m in re.finditer(digram, word):
                score += digrams[digram]
        scores.append(score/len(word)*1000)

    #print(scores)
    print(formatted[scores.index(max(scores))])
    print()
    overall_scores.append(max(scores))
    overall_texts.append(formatted[scores.index(max(scores))])
text = text[::-1]
for key in keys:
    formatted=create(listify(text, key))

    scores = []

    for word in formatted:
        score = 0
        for digram in digrams.keys():
            for m in re.finditer(digram, word):
                score += digrams[digram]
        scores.append(score/len(word)*1000)

    #print(scores)
    print(formatted[scores.index(max(scores))])
    print()
    overall_scores.append(max(scores))
    overall_texts.append(formatted[scores.index(max(scores))])

    formatted=create(listify(col_wise(text,key), key))

    scores = []

    for word in formatted:
        score = 0
        for digram in digrams.keys():
            for m in re.finditer(digram, word):
                score += digrams[digram]
        scores.append(score/len(word)*1000)

    #print(scores)
    print(formatted[scores.index(max(scores))])
    print()
    overall_scores.append(max(scores))
    overall_texts.append(formatted[scores.index(max(scores))])

print()
print("After analysis of all possible texts, the best solution is:")
print(overall_texts[overall_scores.index(max(overall_scores))])
