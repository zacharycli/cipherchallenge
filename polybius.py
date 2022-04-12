alpha = [['a','b','c','d','e'],['f','g','h','i','k'],['l','m','n','o','p'],['q','r','s','t', 'u'],['v','w','x','y','z']]
code = input("> ")#.replace(" ", "")
lasti = ''
for i in (b := code.split(' ')):
    try:
        print(alpha[(int(i[0])-1)%5][(int(i[1])-1)%5], end = '')
    except:
        if lasti == '' and i == '':
            print(i, end = ' ')
        else:
            print(i, end = '')
    lasti=i
