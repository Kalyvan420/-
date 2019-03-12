str = 'Ростов, вкусный, гроза, бобров, Краков'
str = str.split(', ')
for i in range (0, len(str)):
    if str[i][len(str[i])-1]=='в' and str[i][len(str[i])-2]=='о':
        print(str[i])
