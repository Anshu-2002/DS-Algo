def Find(txt):
    l1=[]
    vocabulary=["sun","in","east","doctor","day"]
    for i in txt.split():
        if i in vocabulary and i not in l1:
            l1.append(i)
    return set(l1)
print(Find("the sun rises in the east"))
