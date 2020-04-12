import random as rdn

n = 10
index = range(n)
a_i = []
for i in index:
    a_i.append(rdn.randint(-10,10))

teilSummen = []
nrAdditionen = 0
for i in index:
    for j in index[i:]:
        s = 0
        for k in index[i:j+1]:
            s = s + a_i[k]
            nrAdditionen = nrAdditionen + 1
        teilSummen.append((i+1,j+1,s))
print(a_i)
print(teilSummen, nrAdditionen)

# S_(i,j) = S_(i,1) - S(j-1,1)
teilSummen = []
nrAdditionen = 0
s = []
for i in index:
    teilSummen.append([])
    for j in index[:i+1]:
        dummy = a_i[i]
        if i > 0:
            if j == 0:
                dummy = teilSummen[i - 1][0][2] + dummy
            else:
                dummy = teilSummen[i][0][2] - teilSummen[j - 1][0][2]
        nrAdditionen = nrAdditionen + 1
        teilSummen[i].append((j+1,i+1,dummy))

print(teilSummen,nrAdditionen)











