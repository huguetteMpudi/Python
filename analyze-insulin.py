with open("preproinsulin-seq-clean.txt") as f:
    contents = f.read()
print(len(contents))

with open("lsinsulin-seq-clean.txt", "w") as m:
    m.write(contents[0:24])
m.close()

with open("binsulin-seq-clean.txt", "w") as b:
    b.write(contents[24:54])
b.close()

with open("cinsulin-seq-clean.txt", "w") as c:
    c.write(contents[54:89])
b.close()

with open("ainsulin-seq-clean.txt", "w") as a:
    a.write(contents[89:110])
b.close()
