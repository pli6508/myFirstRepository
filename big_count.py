name = input("Enter file:")
if len(name) < 1:
    name = "SR0752REC-Korsuva.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.strip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[0:20]:
    print(key, val)