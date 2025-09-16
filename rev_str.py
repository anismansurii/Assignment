str = 'abc'
char =[]

for i in str:
    char.append(i)

print(char)

len = len(str)

ans = ''
for i in range(len):
    ans += char[len - i - 1]
print(ans)