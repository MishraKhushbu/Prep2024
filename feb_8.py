import os

the_st = "aabbbcccdddd"

d = {}

for i in range (len(the_st)):
    if the_st[i] not in d:
        d[the_st[i]] = 1
    else:
        d[the_st[i]] += 1

print(d)
