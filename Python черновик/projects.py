#num = int(input())
#binary = ''
#while num > 0:
#    binary = str(num % 2) + binary
#    num //= 2
#print(binary)

#s = 'abcdefg'
#print(s[::-3])

s = input()
a = 0
for i in s:
    if i.islower():
        a += 1
print(a)




n = int(input())
a = 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        a += 1
print(a)




s = input()
maX = 0
b = 0
for i in range(len(s)):
    if s.count(s[i]) >= b:
        b = s.count(s[i])
        maX = s[i]
print(maX)