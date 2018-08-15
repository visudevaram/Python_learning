#Best solution for Social network problem - efficient
#   1. It converts input to dictionaries with groups of 0s, 1s, 2s etc. where key is number and value is groups 
#   2. With in each group, it splits from beginning to end e.g. 1, [1,2,3], 2
#   3. Finally sorts output based on 1st element
counts = [5,2,1,1,2,1]
x = counts[1:]
print(type(counts))
myset = set(x)
u = list(myset)
d = {}
for i in u:
    d[i] = [ind for ind in range(len(x)) if x[ind] == i]

res = [];
print(d)
for k,v in d.items():
    no = int(len(v)/k)
    st = 0 
    for i in range(0,no):
        res = res + [v[st:st+k]]
        st = st + k
z = sorted(res, key=lambda x: x[0])
for s in z:
    if isinstance(s, int):
        print(str(s))
    else:
        print(*s)
