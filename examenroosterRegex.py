import re

with open('lol.txt', 'r') as examenText:
    text = examenText.read()

examenRegex = re.compile(r'.*r0652542.*')


matches = re.findall(examenRegex, text)


f = open('lol.txt','w')

spacieRegex = re.compile(r'\\t')
for i in matches:
    f.write(i + '\n')
    print(i)
    spacieRegex.sub(' ', i)

f.close()