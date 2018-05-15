import re

with open('rooster.txt', 'r') as examenText:
    text = examenText.read()

examenRegex = re.compile(r'.*[vervang dit door uw studentennummer].*')


matches = re.findall(examenRegex, text)


f = open('rooster.txt','w')

spacieRegex = re.compile(r'\\t')
for i in matches:
    f.write(i + '\n')
    print(i)
    spacieRegex.sub(' ', i)

f.close()
