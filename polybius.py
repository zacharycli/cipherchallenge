alpha = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]

code = input("> ").replace(" ", "")

for i in range(0, len(code), 2):
    print(alpha[int(code[i])-1][int(code[i+1])-1], end = '')
