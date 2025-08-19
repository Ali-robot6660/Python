n =int(input())
mylist = []
mylist_res = []
list_sk = []
for i in range(n):
    s = input()
    mylist.append(s)
k = int(input())
for i in range(k):
    sk = input()
    list_sk.append(sk)
    
for j in range(len(mylist)):
    line = mylist[j].lower()
    if all(word in line for word in list_sk):
        mylist_res.append(mylist[j])
print(*mylist_res, sep = '\n')